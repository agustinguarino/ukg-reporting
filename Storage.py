import os

class Storage:
    def __init__(self):
        pass

    def buildsFileExists(self):
        file_path = "C:/Data/builds2.txt"
        return True if os.path.exists(file_path) else False