import os

class Mount:
    def __init__(self, path = "", name = ""):
        self.path = path
        self.name = name
        self.username = os.getlogin()
        self.errors = 0

    #SET
    def setPath(self, path):
        self.path = path.replace("user", self.username).replace('"', "")
        if not(os.path.exists(self.path)):
            self.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("El disco no existe."))

    def setName(self, name):
        self.name = name

    #GET
    def getPath(self):
        return self.path

    def getName(self):
        return self.name