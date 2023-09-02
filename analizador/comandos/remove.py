import os

class Remove:
    def __init__(self, path = ""):
        self.path = path
        self.errors = 0

    #SET
    def setPath(self, path):
        self.path = path.replace("user", "luis_tavico").replace('"', "")
        if (not os.path.exists(self.path)):
            print("¡Error! el archivo no existe.")
            self.errors += 1
        
    #GET
    def getPath(self):
        return self.path