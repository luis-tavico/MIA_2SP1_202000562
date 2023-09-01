class Mkdir:
    def __init__(self, path = "", r = False):
        self.path = path
        self.r = r

    #SET
    def setPath(self, path):
        self.path = path

    def setR(self, r):
        self.r = r

    #GET
    def getPath(self):
        return self.path

    def getR(self):
        return self.r