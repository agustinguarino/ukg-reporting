import requests

buildconsole_url = "https://buildconsole.ulti.io/api/pipeline/654aa1e7340e6379f892796c/0/5?search="

response = requests.get(buildconsole_url)

data = response.json()["builds"]

for i in range(0, len(data)):
    build_state = data[i]["displayStepMap"]["P0 Quality Gate"]["subSteps"][0]["progress"]["state"]
    buildconsole_id = data[i]["_id"]
    build_number = data[i]["buildNumber"]

    print(f"BuildConsole ID: {buildconsole_id} || Build Number: {build_number} || State: {build_state}")

    if "finished" not in build_state:

        # Replace this logic once Storage module is created. Handle file creation, appending to file, removing id from file, etc
        with open("C:/Data/Builds.txt", "a", encoding="utf-8") as file:
            file.write(f"{buildconsole_id},")

        print(f"[{build_number}] Build not finished, saving in file to check again in next execution.")