class Rename:
    def __init__(self, path = "", name = ""):
        self.path = path
        self.name = name

    #SET
    def setPath(self, path):
        self.path = path

    def setName(self, name):
        self.name = name

    #GET
    def getPath(self):
        return self.path

    def getName(self):
        return self.name