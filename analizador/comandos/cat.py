class Cat:
    def __init__(self, fileN = ""):
        self.fileN = fileN

    #SET
    def setFileN(self, fileN):
        self.fileN = fileN

    #GET
    def getFileN(self):
        return self.fileN