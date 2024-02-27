from bs4 import BeautifulSoup
import lxml
from Preprocessing import Preprocessing

class TeamCity:

    def __init__(self):
        pass

    def parseTestsInBuild(self, payload):
        response = []

        data = BeautifulSoup(payload, features="xml")
        tests = data.find_all("testOccurrence")

        for test in tests:
            raw_name = test.get("name")
            name_fields = Preprocessing(str(raw_name)).parseName()

            status = test.get("status")
            duration = test.get("duration")
            muted = test.get("muted")

            data = f"{str(name_fields)}||{status}||{duration}||{muted}"

            if status == "FAILURE":
                # Get stacktrace
                details = test.find("details")
                stacktrace = details.text[:600]

                data = f"{data}||{stacktrace}"
                #response.append(f"{name}||{status}||{duration}||{muted}||{stacktrace}")
            #else:
                #response.append(f"{name}||{status}||{duration}||{muted}")

            response.append(data)

            # TODO: Parse stacktrace to get error category and extra info
        return response
    
    def parseBuildSummary(self, payload):
        response = {}

        data = BeautifulSoup(payload, features="xml")
        summary = data.find("testCounters")

        response["all"] = summary.get("all")
        response["success"] = summary.get("success")
        response["failed"] = summary.get("failed")
        response["muted"] = summary.get("muted")
        response["ignored"] = summary.get("ignored")
        response["newFailed"] = summary.get("newFailed")

        return response
    
    def parseBuildExtraInformation(self, payload):
        response = {}

        data = BeautifulSoup(payload, features="xml")
        
        response["queued_date"] = data.find("queuedDate").text
        response["start_date"] = data.find("startDate").text
        response["finish_date"] = data.find("finishDate").text

        return response