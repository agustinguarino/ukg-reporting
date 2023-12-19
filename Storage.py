import os

class Storage:
    main_path = ""

    def __init__(self):
        self.main_path = "C:/Data"
        if self.buildsFileExists() is False:
            self.__createBuildsFile()

    def __createBuildsFile(self):
        file = open(self.main_path, "w")
        file.close()

    def buildsFileExists(self):
        return True if os.path.exists(f"{self.main_path}/builds.txt") else False
    
    def getBuildsInBuildsFile(self):
        with open(f"{self.main_path}/builds.txt", "r", encoding="utf-8") as file:
            return str(file.read).split(",")
        
    def saveBuildsListToBuildsFile(self, builds_list):
        builds_str = ''.join(str(f"{b},") for b in builds_list)

        with open(f"{self.main_path}/builds.txt", "w", encoding="utf-8") as file:
            file.write(builds_str)
    
    # Save tests data
    
    def __checkBuildPathExistence(self, build_number, folder_path, file_name):
        if os.path.exists(folder_path) is False:
            os.umask(0)
            os.makedirs(folder_path)

            file = open(f"{folder_path}/{file_name}", "w").close()
            
    def saveTestData(self,build_number, tests):
        report_path = f"{self.main_path}/{build_number}"
        report_file_path = f"{report_path}/Tests.csv"

        self.__checkBuildPathExistence(build_number, report_path, "Tests.csv")

        with open(report_file_path, "a", encoding="utf-8") as file:
            for test in tests:
                information = str(test).replace(",", ";").replace("||", ",") + "\n"
                file.write(information)

    def saveBuildSummary(self, build_number, build_summary):
        folder_path = f"{self.main_path}/{build_number}"
        file_name = "BuildSummary.csv"

        self.__checkBuildPathExistence(build_number, folder_path, file_name)

        headers = "ALL, SUCCESS, FAILED, MUTED, IGNORED, NEW FAILED, QUEUED DATE, STARTED DATE, FINISHED DATE"
        data = f"{build_summary['all']}, {build_summary['success']},{build_summary['failed']},{build_summary['muted']},{build_summary['ignored']},{build_summary['newFailed']},"

        with open(f"{folder_path}/{file_name}", "w", encoding="UTF-8") as file:
            file.write(headers + "\n")
            file.write(data)

    def saveBuildExtraInformation(self, build_number, extra_information):
        folder_path = f"{self.main_path}/{build_number}"
        file_name = "BuildSummary.csv"

        self.__checkBuildPathExistence(build_number, folder_path, file_name)

        data = f"{extra_information['queued_date']},{extra_information['start_date']},{extra_information['finish_date']}"
        with open(f"{folder_path}/{file_name}", "a", encoding="UTF-8") as file:
            file.write(data)