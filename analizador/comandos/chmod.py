import os

class Chmod:
    def __init__(self, path = "", ugo = "", r = False):
        self.path = path
        self.ugo = ugo
        self.r = r
        self.username = os.getlogin()

    #SET
    def setPath(self, path):
        self.path = path.replace("user", self.username).replace('"', "")

    def setUgo(self, ugo):
        self.ugo = ugo

    def setR(self, r):
        self.r = r

    #GET
    def getPath(self):
        return self.path

    def getUgo(self):
        return self.ugo

    def getR(self):
        return self.r