from bs4 import BeautifulSoup
import lxml

class TeamCity:

    def __init__(self):
        pass

    def parseTestsInBuild(self, payload):
        response = []

        data = BeautifulSoup(payload, features="xml")
        tests = data.find_all("testOccurrence")

        for test in tests:
            name = test.get("name")
            status = test.get("status")
            duration = test.get("duration")
            muted = test.get("muted")

            response.append(f"{name}||{status}||{duration}||{muted}")

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