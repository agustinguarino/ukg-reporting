import requests
import json
from bs4 import BeautifulSoup

url = "https://buildconsole.ulti.io/api/pipeline/654aa1e7340e6379f892796c/0/5?search="

response = requests.get(url)

builds = response.json()["builds"]
print(str(len(builds)))

build_id = builds[4]["displayStepMap"]["P0 Quality Gate"]["subSteps"][0]["progress"]["id"]
print(f"Build ID: {build_id}")

url = f"https://teamcity.dev.us.corp/app/rest/testOccurrences?locator=build:({build_id}),status:FAILURE,count:500&fields=testOccurrence(id,name,status,muted,duration)"
session = requests.session()
headers = {
    'Authorization' : 'Bearer eyJ0eXAiOiAiVENWMiJ9.NXdsUUpyMEM4LW14T29oWEE3VDZ3MWNrZnFF.NDJjOGRmMmEtN2JkNi00ZWQ3LWE2ODAtNzE4NTMyZWIxN2M1'
}
session.headers = headers

response = session.get(url)
print(response)

soup = BeautifulSoup(response.content, 'xml')
occurrences = soup.find_all('testOccurrence')
for occ in occurrences:
    test_name = occ.get("name")
    test_duration = occ.get("duration")
    data = f"Test Name: {test_name} || Test Duration: {test_duration}"
    print(data)