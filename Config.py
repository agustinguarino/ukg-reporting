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
                variable_name = line[0]
                variable_value = line[1]

                self.config[variable_name] = variable_value