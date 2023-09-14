
class Mkfs:
    def __init__(self, id = "", type = "full", fs = "2fs"):
        self.id = id
        self.type = type
        self.fs = fs

    #SET
    def setId(self, id):
        self.id = id

    def setType(self, type):
        self.type = type

    def setFs(self, fs):
        self.fs = fs

    #GET
    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def getFs(self):
        return self.fs