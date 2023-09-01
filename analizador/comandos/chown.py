class Chown:
    def __init__(self, path = "", user = "", r = ""):
        self.path = path
        self.user = user
        self.r = r

    #SET
    def setPath(self, path):
        self.path = path
    
    def setUser(self, user):
        self.user = user 

    def setR(self, r):
        self.r = r

    #GET
    def getPath(self):
        return self.path
    
    def getUser(self):
        return self.user
    
    def getR(self):
        return self.r