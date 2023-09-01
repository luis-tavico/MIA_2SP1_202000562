class Edit:
    def __init__(self, path = "", cont = ""):
        self.path = path
        self.cont = cont

    #SET
    def setPath(self, path):
        self.path = path.replace("user", "luis_tavico").replace('"', "")

    def setCont(self, cont):
        self.cont = cont.replace("user", "luis_tavico").replace('"', "")

    #GET
    def getPath(self):
        return self.path
    
    def getCont(self):
        return self.cont