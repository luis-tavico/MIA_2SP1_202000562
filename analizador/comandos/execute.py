import os

class Execute:
    def __init__(self, path = ""):
        self.path = path
        self.username = os.getlogin()
        self.errors = 0

    #SET
    def setPath(self, path):
        self.path = path.replace("user", self.username).replace('"', "")
        if not(os.path.exists(self.path)):
            self.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("El archivo no existe."))

    #GET
    def getPath(self):
        return self.path