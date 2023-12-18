import requests
from Config import Config

class API:
    config = ""

    def __init__(self):
        self.config = Config().getConfig()

    def getBuildConsoleBuilds(self):
        url = self.config["bc_pipeline_api_url"]
        return requests.get(url).json()