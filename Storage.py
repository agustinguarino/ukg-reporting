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
            
    def saveTestData(self,build_number, tests):
        report_path = f"{self.main_path}/{build_number}"
        report_file_path = f"{report_path}/tests.csv"

        if os.path.exists(report_path) is False:
            os.umask(0)
            os.makedirs(report_path)
            file = open(report_file_path, "w").close()

        with open(report_file_path, "a", encoding="utf-8") as file:
            for test in tests:
                information = str(test).replace(",", ";").replace("||", ",") + "\n"
                file.write(information)
