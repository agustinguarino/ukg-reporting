class Builds:
    payload = ""
    information = {}

    def __init__(self, payload):
        self.payload = payload

    def getInformation(self):
        return self.information
    
    def analyzeBuildConsoleGeneralBuilds(self):
        data = self.payload["builds"]
        builds_amount = len(data)

        for i in range(0, builds_amount):
            build_id = data[i]["_id"]
            state = data[i]["displayStepMap"]["P0 Quality Gate"]["subSteps"][0]["progress"]["state"]

            self.information[build_id] = state

    def analyzeBuildConsoleSpecificBuild(self):
        data = self.payload
        build_id = data["_id"]
        build_state = data["displayStepMap"]["P0 Quality Gate"]["subSteps"][0]["progress"]["state"]
        teamcity_id = data["displayStepMap"]["P0 Quality Gate"]["subSteps"][0]["progress"]["id"]

        self.information["build_id"] = build_id
        self.information["build_state"] = build_state
        self.information["teamcity_id"] = teamcity_id