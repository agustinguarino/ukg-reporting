from datetime import datetime, timedelta
from Config import Config
import pymsteams
import math

class Messaging:
    config = ""
    message = ""

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

        self.message = pymsteams.connectorcard(webhook_url)

        # create the section
        p0_section = pymsteams.cardsection()

        # Activity Elements
        p0_section.activityTitle("P0 Quality Gate:")

        # Define which image to use for the section (success or fail) and the color of the card (green or red)
        if "SUCCESS" in str(build_status):
            # Successful build
            p0_section.activityImage(self.config["build_success_image"])
            self.message.color("10eb10")

        else:
            # Failed build
            p0_section.activityImage(self.config["build_fail_image"])
            self.message.color("a83e32")

        # Build dates in correct format and time deltas
        queued_date = datetime.strptime(datetime.strptime(build_extra_information['queued_date'], '%Y%m%dT%H%M%S%z').strftime('%Y/%m/%d %H:%M:%S'), '%Y/%m/%d %H:%M:%S')
        start_date = datetime.strptime(datetime.strptime(build_extra_information['start_date'], '%Y%m%dT%H%M%S%z').strftime('%Y/%m/%d %H:%M:%S'), '%Y/%m/%d %H:%M:%S')
        finish_date = datetime.strptime(datetime.strptime(build_extra_information['finish_date'], '%Y%m%dT%H%M%S%z').strftime('%Y/%m/%d %H:%M:%S'), '%Y/%m/%d %H:%M:%S')

        queued_to_finish = finish_date - queued_date
        start_to_finish = finish_date - start_date

        #pass_rate = (int(build_summary['success']) * 100) / (int(build_summary['all']) - int(build_summary['muted']))
        pass_rate = (int(build_summary['success']) * 100) / (int(build_summary['all']) - int(build_summary['muted'])) if int(build_summary['all']) > 0 else 0


        # Facts are key value pairs displayed in a list.
        p0_section.addFact("All tests executed:", f"{build_summary['all']}") # Add difference with last build (+5)
        p0_section.addFact("Tests passed:", f"{build_summary['success']} ({self.__truncate(pass_rate, 2)}%)")
        p0_section.addFact("Tests failed:", f"{build_summary['failed']}") # Add difference with last build (-2)
        p0_section.addFact("Tests muted:", f"{build_summary['muted']}") # Add difference with last build (+0)
        p0_section.addFact("Ignored tests:", f"{build_summary['ignored']}") # Add difference with last build (+0)
        p0_section.addFact("New failed tests:", f"{build_summary['newFailed']}") # Add difference with last build (+1)
        p0_section.addFact("Teams with failures:", f"{failure_teams}")
        p0_section.addFact("-", " ")
        p0_section.addFact("Queded date:", f"{str(queued_date)}")
        p0_section.addFact("Started date:", f"{str(start_date)}")
        p0_section.addFact("Finish date:", f"{str(finish_date)}")
        p0_section.addFact("-", " ")
        p0_section.addFact("From queue to finish:", f"{str(queued_to_finish)}")
        p0_section.addFact("From start to finish:", f"{str(start_to_finish)}")

        # Section Images
        #p0_section.addImage("http://i.imgur.com/c4jt321l.png", ititle="Failure build")

        self.message.addSection(p0_section)

        self.message.title(bc_build_number)
        self.message.text(" ")

        self.message.addLinkButton("Open P0 in TeamCity", f"https://teamcity.dev.us.corp/buildConfiguration/UltiPro_V12_4Integration_1Domains_P0QualityGate_00RunTests/{tc_build_id}?buildTab=tests")
        self.message.addLinkButton("Open full report", "https://google.com/")



        # P1 Quality Gate section - IN PROGRESS -
        p1_section = pymsteams.cardsection()
        # Activity Elements
        p1_section.activityTitle("P1 Quality Gate:")
        p1_section.activityImage(self.config["build_success_image"])
        p1_section.activitySubtitle("Work in progress...")

        self.message.addSection(p1_section)

    def sendMessage(self):
        self.message.send()