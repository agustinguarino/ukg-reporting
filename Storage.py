import os

class Storage:
    root_path = "C:/Users/agustinignacio.guari/Desktop/OneDrive - UKG/ukg-reporting/"
    builds_path = f"{root_path}Builds/"

    def __init__(self):
        if self.buildsFileExists() is False:
            self.__createBuildsFile()

    def __createBuildsFile(self):
        file = open(f"{self.root_path}builds.txt", "w")
        file.close()

    def buildsFileExists(self):
        return True if os.path.exists(f"{self.root_path}builds.txt") else False
    
    def getBuildsInBuildsFile(self):
        list = []
        with open(f"{self.root_path}builds.txt", "r", encoding="utf-8") as file:
            builds = file.readlines()
            return builds

    def addBuildToBuildsFile(self, build_id):
        builds = self.getBuildsInBuildsFile()
        if build_id in builds:
            return False
        else:
            with open(f"{self.root_path}builds.txt", "a") as file:
                file.write(f"{build_id}\n")

    def removeBuildFromBuildsFile(self, build_id):
        builds = list(map(lambda x: x.replace("\n", ""), self.getBuildsInBuildsFile()))

        if build_id in builds:
            builds.remove(build_id)
            
            with open(f"{self.root_path}builds.txt", "w") as file:
                builds_str = ''.join([str(build + "\n") for build in builds])
                file.writelines(builds_str)

    def buildExistsInBuildFile(self, build_id):
        builds = list(map(lambda x: x.replace("\n", ""), self.getBuildsInBuildsFile()))

        return True if build_id in builds else False
    
    # Save tests in build
    def saveTestsInBuild(self, build_id, tests):
        file_path = f"{self.builds_path}{build_id}/Tests.csv"
        headers = "Test name, Package, Team, Status, Duration, Muted, Stacktrace"

        # Create file
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        f = open(file_path, "w").close()

        with open(file_path, "a") as file:
            file.write(headers + "\n")

        for test in tests:
            #test_list = str(test).strip().replace(",", ";").replace("\n", "").split("||")
            test_list = (" ".join(str(test).replace(",", ";").replace("\n", "").split())).split("||")

            data = ",".join(str(x) for x in test_list)
            with open(file_path, "a") as file:
                file.write(data + "\n")


    def saveBuildExtraInformation(self, build_id, build_summary, extra_information, build_status):
        file_path = f"{self.builds_path}{build_id}/BuildSummary.csv"

        headers = "Queued date, Start date, Finish date, Build State, All, Success, Failed, Muted, Ignored, New Failed"
        data = f"{extra_information['queued_date']},{extra_information['start_date']},{extra_information['finish_date']},{str(build_status)},{build_summary['all']},{build_summary['success']},{build_summary['failed']},{build_summary['muted']},{build_summary['ignored']},{build_summary['newFailed']}"

        with open(file_path, "w") as file:
            file.write(headers + "\n")
            file.write(data)