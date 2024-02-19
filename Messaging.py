from datetime import datetime, timedelta
from Config import Config
import pymsteams
import math
import json
import requests

class Messaging:
    config = ""
    webhook_url = ""
    payload = ""

    def __init__(self) -> None:
        self.config = Config().getConfig()

    def __truncate(self, number, decimals):
        """
        Returns a value truncated to a specific number of decimal places.
        """
        if not isinstance(decimals, int):
            raise TypeError("decimal places must be an integer.")
        elif decimals < 0:
            raise ValueError("decimal places has to be 0 or more.")
        elif decimals == 0:
            return math.trunc(number)

        factor = 10.0 ** decimals
        return math.trunc(number * factor) / factor

    def craftMessage(self, webhook_url, build_summary, build_extra_information, failure_teams, tc_build_id, bc_build_number, build_status):

        self.webhook_url = webhook_url

        # Define which image to use for the section (success or fail) and the color of the card (green or red)
        if "SUCCESS" in str(build_status):
            # Successful build
            p0_image = self.config["build_success_image"]

        else:
            # Failed build
            p0_image = self.config["build_fail_image"]

        # All tests fields
        total_tests = build_summary['all']

        pass_rate = (int(build_summary['success']) * 100) / (int(build_summary['all']) - int(build_summary['muted'])) if int(build_summary['all']) > 0 else 0
        tests_passed = f"{build_summary['success']} ({self.__truncate(pass_rate, 2)}%)"

        tests_failed = build_summary['failed']
        muted_tests = build_summary['muted']
        ignored_tests = build_summary['ignored']
        new_failed_tests = build_summary['newFailed']

        # Build dates in correct format and time deltas
        queued_date = datetime.strptime(datetime.strptime(build_extra_information['queued_date'], '%Y%m%dT%H%M%S%z').strftime('%Y/%m/%d %H:%M:%S'), '%Y/%m/%d %H:%M:%S')
        start_date = datetime.strptime(datetime.strptime(build_extra_information['start_date'], '%Y%m%dT%H%M%S%z').strftime('%Y/%m/%d %H:%M:%S'), '%Y/%m/%d %H:%M:%S')
        finish_date = datetime.strptime(datetime.strptime(build_extra_information['finish_date'], '%Y%m%dT%H%M%S%z').strftime('%Y/%m/%d %H:%M:%S'), '%Y/%m/%d %H:%M:%S')

        queued_to_finish = finish_date - queued_date
        start_to_finish = finish_date - start_date

        #pass_rate = (int(build_summary['success']) * 100) / (int(build_summary['all']) - int(build_summary['muted']))
        pass_rate = (int(build_summary['success']) * 100) / (int(build_summary['all']) - int(build_summary['muted'])) if int(build_summary['all']) > 0 else 0

        teamcity_url = f"https://teamcity.dev.us.corp/buildConfiguration/UltiPro_V12_4Integration_1Domains_P0QualityGate_00RunTests/{tc_build_id}?buildTab=tests"


        # Pase teams with failures and tags
        msteams_entities = []
        teams_array = []
        teams_poc = Config().getPOCsTable()

        for team in failure_teams.keys():
            print(f"Processing: {team}")
            if team in teams_poc.keys():
                if len(teams_poc[team]) <= 10:
                    #teams_with_failures.append(f"{team}: {failure_teams[team]}")
                    teams_array.append(f"{team} ({failure_teams[team]})")

                else:
                    #teams_with_failures.append(f"<at>{team}</at>: {failure_teams[team]}")
                    teams_array.append(f"<at>{team}</at> ({failure_teams[team]})")

                    team_object = {
                        "type": "mention",
                        "text": f"<at>{team}</at>",
                        "mentioned": {
                            "id": f"{teams_poc[team]}",
                            "name": f"{team}"
                        }
                    }

                    msteams_entities.append(team_object)

        print(f"Entities: {str(msteams_entities).strip()}")
        teams_with_failures = ", ".join(teams_array)

        # Get payload and format
        payload = self.config["teams_card_payload"]

        payload = payload.replace("%build_version%", bc_build_number)
        payload = payload.replace("%total_tests%", total_tests)
        payload = payload.replace("%tests_passed%", tests_passed)
        payload = payload.replace("%tests_failed%", tests_failed)
        payload = payload.replace("%muted_tests%", muted_tests)
        payload = payload.replace("%ignored_tests%", ignored_tests)
        payload = payload.replace("%new_failed_tests%", new_failed_tests)
        payload = payload.replace("%teams_with_failures%", str(teams_with_failures))
        payload = payload.replace("%queued_date%", str(queued_date))
        payload = payload.replace("%started_date%", str(start_date))
        payload = payload.replace("%finish_date%", str(finish_date))
        payload = payload.replace("%from_queue_to_finish%", str(queued_to_finish))
        payload = payload.replace("%from_start_to_finish%", str(start_to_finish))
        payload = payload.replace("%teamcity_url%", teamcity_url)
        payload = payload.replace("%p0_image%", p0_image)
        payload = payload.replace("%msteams_entities%", str(msteams_entities).replace("'", "\""))

        #with open("test.txt", "w") as file:
            #file.write(payload)

        self.payload = json.loads(payload)

        # Section Images
        #p0_section.addImage("http://i.imgur.com/c4jt321l.png", ititle="Failure build")

    def sendMessage(self):
        req = requests.post(url=self.webhook_url, json=self.payload)
        print(f"Request status: {req.status_code}")