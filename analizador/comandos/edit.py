import os

class Edit:
    def __init__(self, path = "", cont = ""):
        self.path = path
        self.cont = cont
        self.username = os.getlogin()

    #SET
    def setPath(self, path):
        self.path = path.replace("user", self.username).replace('"', "")

    def setCont(self, cont):
        self.cont = cont.replace("user", self.username).replace('"', "")

    #GET
    def getPath(self):
        return self.path
    
    def getCont(self):
        return self.cont