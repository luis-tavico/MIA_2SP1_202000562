import os

class Mkdir:
    def __init__(self, path = "", r = False):
        self.path = path
        self.r = r
        self.username = os.getlogin()

    #SET
    def setPath(self, path):
        self.path = path.replace("user", self.username).replace('"', "")

    def setR(self, r):
        self.r = r

    #GET
    def getPath(self):
        return self.path

    def getR(self):
        return self.r