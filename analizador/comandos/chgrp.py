class Chgrp:
    def __init__(self, user = "", grp = ""):
        self.user = user
        self.grp = grp

    #SET
    def setUser(self, user):
        self.user = user

    def setGrp(self, grp):
        self.grp = grp

    #GET
    def getUser(self):
        return self.user

    def getGrp(self):
        return self.grp