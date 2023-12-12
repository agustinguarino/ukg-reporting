import os

class Storage:
    file_path = ""

    def __init__(self):
        self.file_path = "C:/Data/builds.txt"
        pass

    def buildsFileExists(self):
        return True if os.path.exists(self.file_path) else False
    
    def getBuildsInBuildsFile(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return str(file.read).split(",")
        
    def saveBuildsListToBuildsFile(self, builds_str):
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(builds_str)