import os

class Rep:
    def __init__(self, name = "", path = "", id = "", ruta = ""):
        self.name = name
        self.path = path
        self.id = id
        self.ruta = ruta
        self.username = os.getlogin()
        self.errors = 0


    #SET
    def setName(self, name):
        self.name = name

    def setPath(self, path):
        self.path = path.replace("user", self.username).replace('"', "")
        if not(os.path.exists(self.path)):
            carpetas = os.path.dirname(self.path)
            if not(os.path.exists(carpetas)):
                os.makedirs(carpetas)

    def setId(self, id):
        self.id = id

    def setRuta(self, ruta):
        self.ruta = ruta

    #GET
    def getName(self):
        return self.name

    def getPath(self):
        return self.path

    def getId(self):
        return self.id

    def getRuta(self):
        return self.ruta