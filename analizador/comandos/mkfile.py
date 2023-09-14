import os

class Mkfile:
    def __init__(self, path = "", r = False, size = 0, cont = ""):
        self.path = path
        self.r = r
        self.size = size
        self.cont = cont
        self.username = os.getlogin()
        self.errors = 0

    #SET
    def setPath(self, path):
        self.path = path.replace("user", self.username).replace('"', "")

    def setR(self, r):
        self.r = r

    def setSize(self, size):
        self.size = size

    def setCont(self, cont):
        self.cont = cont.replace("user", self.username).replace('"', "")
        if (not os.path.exists(self.path)):
            print("¡Error! el archivo no existe.")
            self.errors += 1

    #GET
    def getPath(self):
        return self.path

    def getR(self):
        return self.r

    def getSize(self):
        return self.size

    def getCont(self):
        return self.cont