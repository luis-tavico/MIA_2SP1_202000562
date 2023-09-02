import os

class Cat:
    def __init__(self, paths = []):
        self.paths = paths
        self.errors = 0

    #SET
    def setPathFile(self, fileN):
        fileN = fileN.replace("user", "luis_tavico").replace('"', "")
        if (not os.path.exists(fileN)):
            print("¡Error! el archivo no existe.")
            self.errors += 1
        self.paths.append(fileN)

    #GET
    def getPathFiles(self):
        return self.paths