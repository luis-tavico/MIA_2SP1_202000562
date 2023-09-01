class chmod:
    def __init__(self, path = "", ugo = "", r = ""):
        self.path = path
        self.ugo = ugo
        self.r = r

    #SET
    def setPath(self, path):
        self.path = path

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