from Preprocessing import Preprocessing
from Messaging import Messaging
from Environment import Environment
from Logger import Logger
from API import API
from Builds import Builds
from Storage import Storage
from TeamCity import TeamCity

"""
TODO: Separate processes - build detection, reporting for p0, reporting for p1, reports, all in different files/modules.
TODO: Move Teams Table to OneDrive folder so changes can be automatically implemented
TODO: Add POCs to Teams Table. Same thing as config, but read column 2 and 3, construct dictionary, add function to Storage module.
TODO: Add stataus_text from api response to build summary, and create an alert in message in case of runner failure.
"""

from datetime import datetime
from time import sleep

build_ids = []

def run():
    bc_builds = API().getBuildConsoleBuilds()
    builds_state = Builds(bc_builds).analyzeBuildConsoleGeneralBuilds()

    Logger(Logger.INFO, f"Builds state: {builds_state}")

    for build in builds_state.keys():
        Logger(Logger.INFO, f"{build} status is: {builds_state[build]}.")

        if "failure" in builds_state[build]:
            Logger(Logger.WARNING, f"Build state for build {build} came as False (failure), skipping loop iteration.")
            continue

        if not builds_state[build] == "finished" and build not in build_ids:
            Logger(Logger.HIGH, f"New build detected: {build}")
            build_ids.append(build)


    builds = build_ids
    #builds.append("65c16c787a8c7695bf327c16\n")

    for build in builds:
        build_bc_id = build.replace("\n", "")
        Logger(Logger.INFO, f"Processing {build_bc_id}.")

        build_result = API().getBuildConsoleSpecificBuild(build_bc_id)
        build_data = Builds(build_result).analyzeBuildConsoleSpecificBuild()

        if build_data is False:
            Logger(Logger.WARNING, f"Failure detected when anaylizing specific build ({build_bc_id}), skipping loop iteration.")
            continue

        Logger(Logger.INFO, f"{build_data['teamcity_id']} is {build_data['build_state']}")

        if build_data['build_state'] == "finished":
        #if True:
            #build_data["teamcity_id"] = "54228319" # Lot of failures - 49 from Payroll
            #build_data["teamcity_id"] = "54131718" # Success
            #build_data["teamcity_id"] = "54426229" # Different failures

            Logger(Logger.HIGH, f"Launching reporting for build {build_data['teamcity_id']} ({build_data['build_state']})")
            #Launch reporting here

            build_id = build_data["teamcity_id"]

            tests = API().getTestsInBuild(build_id)
            parsed_tests = TeamCity().parseTestsInBuild(tests)

            Storage().saveTestsInBuild(build_id, parsed_tests)

            # Build summary and extra information
            Logger(Logger.INFO, f"Saving build extra information - {build_bc_id}")

            build_summary = API().getBuildSummary(build_id)
            parsed_build_summary = TeamCity().parseBuildSummary(build_summary)

            extra_information = API().getBuildExtraInformation(build_id)
            parsed_extra_information = TeamCity().parseBuildExtraInformation(extra_information)

            Storage().saveBuildExtraInformation(build_id, parsed_build_summary, parsed_extra_information, build_data["build_status"])
            Logger(Logger.INFO, f"Finished saving build extra information - {build_bc_id}")

            Logger(Logger.INFO, f"Starting teams message process - {build_bc_id}")

            failure_teams = Preprocessing("test").getTeamsWithFailures(parsed_tests)
            webhook_url = Environment().getWebhookURL("TEAMS_GENERAL_WEBHOOK_URL")

            message = Messaging()
            message.craftMessage(webhook_url, parsed_build_summary, parsed_extra_information, failure_teams, build_data["teamcity_id"], build_data["buildconsole_number"], build_data["build_status"])
            message.sendMessage()

            Logger(Logger.INFO, f"Finalizing teams message process - {build_bc_id}")

            Logger(Logger.INFO, f"Finalizing build reporting for build {build_bc_id}.")

            build_ids.remove(build)
            
    Logger(Logger.INFO, f"Waiting 1 hour before running again.")

    sleep(60 * 60)
    run()


# Run
run()

