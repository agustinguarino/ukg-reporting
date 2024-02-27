from datetime import datetime

class Logger:
    HIGH = "HIGH"
    WARNING = "WARNING"
    INFO = "INFO"   

    format = "(*type*) [*date*] - *message*"

    def __init__(self, type, message):
        self.__logMessage(type, message)

    def __getDate(self):
        return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    def __logMessage(self, type, message):
        date = self.__getDate()

        data = self.format.replace("*type*", type).replace("*date*", date).replace("*message*", message)
        print(data)

    def separator(self):
        type = self.INFO
        message = "-------------------------------------------------------------------------"

        self.__logMessage(type, message)

    def newLine(self):
        type = self.INFO
        message = " "

        self.__logMessage(type, message)

    