import os
from dotenv import load_dotenv

class Environment:
    def __init__(self):
        load_dotenv()

    def getEnvironmentName(self):
        return os.getenv("ENVIRONMENT_NAME")
    
    def getTeamcityToken(self):
        return os.getenv("TEAMCITY_TOKEN")
    
    def getWebhookURL(self, webhook_name):
        return os.getenv(webhook_name)