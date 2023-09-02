class Rename:
    def __init__(self, path = "", name = ""):
        self.path = path
        self.name = name

    #SET
    def setPath(self, path):
        self.path = path.replace("user", "luis_tavico").replace('"', "")

    def setName(self, name):
        self.name = name.replace('"', "")

    #GET
    def getPath(self):
        return self.path

    def getName(self):
        return self.name