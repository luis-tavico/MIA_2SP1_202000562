class Remove:
    def __init__(self, path = ""):
        self.path = path

    #SET
    def setPath(self, path):
        self.path = path.replace("user", "luis_tavico")

    #GET
    def getPath(self):
        return self.path