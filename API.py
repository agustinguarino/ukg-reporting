import requests
from Config import Config
from Environment import Environment

class API:
    config = ""
    token = ""

    def __init__(self):
        self.config = Config().getConfig()
        self.token = Environment().getTeamcityToken()

    def getBuildConsoleBuilds(self):
        url = self.config["bc_pipeline_api_url"]
        return requests.get(url).json()
    
    def getBuildConsoleSpecificBuild(self, build_id):
        url = self.config["bc_build_api_url"] + str(build_id)
        return requests.get(url).json()
    
    # TeamCity calls

    def getTestsInBuild(self, teamcity_id):
        url = self.config["tc_tests_api_url"].replace("[build_id]", str(teamcity_id))

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