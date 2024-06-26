import os

class Copy:
    def __init__(self, path = "", destino = ""):
        self.path = path
        self.destino = destino
        self.username = os.getlogin()

    #SET
    def setPath(self, path):
        self.path = path.replace("user", self.username).replace('"', "")

    def setDestino(self, destino):
        self.destino = destino.replace("user", self.username).replace('"', "")

    #GET
    def getPath(self):
        return self.path
    
    def getDestino(self):
        return self.destino