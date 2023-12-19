import os

class Storage:
    main_path = ""

    def __init__(self):
        self.main_path = "C:/Data"
        if self.buildsFileExists() is False:
            self.__createBuildsFile()

    def __createBuildsFile(self):
        file = open(self.file_path, "w")
        file.close()

    def buildsFileExists(self):
        return True if os.path.exists(f"{self.main_path}/builds.txt") else False
    
    def getBuildsInBuildsFile(self):
        with open(f"{self.file_path}/builds.txt", "r", encoding="utf-8") as file:
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
        report_file_path = f"{report_path}/tests.csv"

        self.__checkBuildPathExistence(build_number, report_path, "tests.csv")

        with open(report_file_path, "a", encoding="utf-8") as file:
            for test in tests:
                information = str(test).replace(",", ";").replace("||", ",") + "\n"
                file.write(information)