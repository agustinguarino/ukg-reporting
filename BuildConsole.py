import requests
import json
from bs4 import BeautifulSoup

buildconsole_url = "https://buildconsole.ulti.io/api/pipeline/654aa1e7340e6379f892796c/0/5?search="

response = requests.get(buildconsole_url)

data = response.json()["builds"]

for i in range(0, len(data)):
    buildconsole_id = data[i]["_id"]
    build_number = data[i]["buildNumber"]
    build_state = data[i]["displayStepMap"]["P0 Quality Gate"]["subSteps"][0]["progress"]["state"]
    print(f"BuildConsole ID: {buildconsole_id} || Build Number: {build_number} || State: {build_state}")