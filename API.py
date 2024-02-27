import requests
from Config import Config
from Environment import Environment

class API:
    config = ""
    token = ""
    pipeline_url = ""

    def __init__(self, pipeline_name):
        self.config = Config().getConfig()
        self.token = Environment().getTeamcityToken()
        self.pipeline_url = self.__getPipelineURL(pipeline_name)

    def __getPipelineURL(self, pipeline_name):
        # Set StepMap name depending on pipeline name
        pipeline_url = ""
        if pipeline_name == "UKGPro Core Domains":
            pipeline_url = self.config["bc_core_pipeline_api_url"]

        elif pipeline_name == "UKGPro Core Quality Gate":
            pipeline_url = self.config["bc_pipeline_api_url"]

        else:
            pipeline_url = "Failed"
            print("Failed to get pipeline URL.")
        
        print(f"API URL: {pipeline_url}")
        return pipeline_url

    def getBuildConsoleBuilds(self):
        url = self.pipeline_url
        return requests.get(url).json()
    
    def getBuildConsoleSpecificBuild(self, build_id):
        url = self.config["bc_build_api_url"] + str(build_id)
        return requests.get(url).json()
    
    # TeamCity calls

    def getTestsInBuild(self, teamcity_id):
        url = self.config["tc_tests_api_url"].replace("[build_id]", str(teamcity_id))
        print("URL: " + url)

        headers = {
            "Authorization": self.token
        }

        session = requests.session()
        session.headers = headers

        return session.get(url).content
    
    def getBuildSummary(self, teamcity_id):
        url = self.config["tc_build_summary_api_url"].replace("[build_id]", str(teamcity_id))
        
        headers = {
            "Authorization": self.token
        }

        session = requests.session()
        session.headers = headers

        return session.get(url).content
    
    def getBuildExtraInformation(self, teamcity_id):
        url = self.config["tc_extra_info_api_url"].replace("[build_id]", str(teamcity_id))

        headers = {
            "Authorization": self.token
        }

        session = requests.session()
        session.headers = headers

        return session.get(url).content