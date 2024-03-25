class Builds:
    payload = ""
    stepMapName = ""
    information = {}

    def __init__(self, payload, pipeline_name):
        self.payload = payload
        self.stepMapName = self.__getStepMapName(pipeline_name)

    def __getStepMapName(self, pipeline_name):
        # Set StepMap name depending on pipeline name
        stepMapName = ""
        if pipeline_name == "UKGPro Core Domains":
            stepMapName = "Build Summary"

        elif pipeline_name == "UKGPro Core Quality Gate":
            stepMapName = "P0 Quality Gate"

        else:
            stepMapName = "Failed"
            print("Failed to get StepMap Name.")
        
        return stepMapName

    def getInformation(self):
        return self.information
    
    def analyzeBuildConsoleGeneralBuilds(self):
        # Clear dictiionary before populating with new data
        self.information = {}

        stepMapName = self.stepMapName

        data = self.payload["builds"]
        builds_amount = len(data)

        for i in range(0, builds_amount):
            build_id = data[i]["_id"]
            
            # If the build is really really new, it maight not contain the progress object in the response
            try:
                state = data[i]["displayStepMap"][stepMapName]["subSteps"][0]["progress"]["state"]

                self.information[build_id] = state
            except Exception as e:
                print(f"Error: {e}")
                self.information[build_id] = "failure"

        # Clear keys from dict
        keys = ["build_id", "build_state", "teamcity_id", "buildconsole_number", "build_status"]
        for key in keys:
            if key in self.information:
                self.information.pop(key)

        return self.information

    def analyzeBuildConsoleSpecificBuild(self):
        stepMapName = self.stepMapName
        print(f"Step Map Name: {stepMapName}")

        data = self.payload
        try:
            build_id = data["_id"]
            build_state = data["displayStepMap"][f"{stepMapName}"]["subSteps"][0]["progress"]["state"]
            build_status = data["displayStepMap"][f"{stepMapName}"]["subSteps"][0]["progress"]["status"]
            teamcity_id = data["displayStepMap"][f"{stepMapName}"]["subSteps"][0]["progress"]["id"]
            buildconsole_number = data["buildNumber"]

            self.information["build_id"] = build_id
            self.information["build_state"] = build_state
            self.information["build_status"] = build_status
            self.information["teamcity_id"] = teamcity_id
            self.information["buildconsole_number"] = buildconsole_number

            return self.information
        except Exception as e:
            print(f"Exception: {e} // {str(e)}")
            return False