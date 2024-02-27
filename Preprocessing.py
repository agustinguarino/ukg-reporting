from Config import Config

class Preprocessing:
    data_string = ""
    type = ""

    def __init__(self, data_string):
        self.data_string = data_string
        self.__getType()

    def __getType(self):
        if "Echo" in str(self.data_string).split(": ")[0]:
            self.type = "Echo"
        
        elif "UltiPro.NET" in str(self.data_string).split(": ")[0]:
            self.type = "Integration"

    def parseName(self):
        response = ""
        test_name = ""
        package = ""
        team_name = ""

        # Get test name
        if "(" in str(self.data_string):
            arguments = str(self.data_string).split(": ")
            for argument in arguments:
                if "(" in str(argument):
                    index = arguments.index(argument)
                    test_name = " ".join(str(x) for x in arguments[index:None])
                    break

        else:
            test_name = self.data_string.split(": ")[-1]

        #print("Test name: " + test_name)
        
        # Get Package
        if len(self.data_string.split(": ")[0].split('\\')) > 1:
            package = self.data_string.split(": ")[0].split('\\')[4]

        else:
            package = self.data_string.split(": ")[0]

        #print("Package: " + package)


        # Get Team name
        teams_table = Config().getTeamsTable()
        
        for key in teams_table.keys():
            if str(key) in package:
                team_name = str(teams_table[key]) 

        #print("Team name: " + team_name)

        response = f"{test_name}||{package}||{team_name}"
        return response
    
    def getTeamsWithFailures(self, tests):
        teams = []
        teams_failures = {}

        for test in tests:
            test_data = str(test).split("||")
            #print(f"Test Status: {str(test_data[3])}")
            #print(f"Team name: {str(test_data[2])}")
            #print(f"Muted status: {str(test_data[5])}")

            # If test status is FAILURE, and team is not already in array, and test is NOT muted
            #if "FAILURE" in str(test_data[3]) and str(test_data[2]) not in teams and "true" not in str(test_data[5]):
                #teams.append(str(test_data[2]))

            if "FAILURE" in str(test_data[3]) and "true" not in str(test_data[5]):
                if str(test_data[2]) not in teams_failures.keys():
                    teams_failures[str(test_data[2])] = 1
                else:
                    teams_failures[str(test_data[2])] += 1

        #return teams
        return teams_failures

