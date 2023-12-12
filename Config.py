import csv

class Config():
    config_file_path = "Config.csv"
    config = {}

    def __init__(self):
        pass

    def readConfigFile(self):
        with open(self.config_file_path, mode="r", ) as file:
            csv_file = csv.reader(file)
            next(file)

            for line in csv_file:
                print(line)