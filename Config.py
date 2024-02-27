import csv

class Config():
    config_file_path = "Config.csv"
    teams_table_path = "Teams Table.csv"
    failures_table_path = "Failures Table.csv"

    def __init__(self):
        pass

    def __readFile(self, file_path):
        config = {}

        with open(file_path, mode="r", ) as file:
            csv_file = csv.reader(file)
            next(file)

            for line in csv_file:
                variable_name = line[0]
                variable_value = line[1]

                config[variable_name] = variable_value

        return config
    
    def getConfig(self):
        return self.__readFile(self.config_file_path)
    
    def getTeamsTable(self):
        return self.__readFile(self.teams_table_path)
    
    def getPOCsTable(self):
        pocs = {}

        with open(self.teams_table_path, mode="r", ) as file:
            csv_file = csv.reader(file)
            next(file)

            for line in csv_file:
                variable_name = line[1]
                variable_value = line[2]

                pocs[variable_name] = variable_value

        return pocs
    
    def getFailuresTable(self):
        return self.__readFile(self.failures_table_path)