import struct

class Login:
    def __init__(self, user = "", password = "", id = ""):
        self.user = user
        self.password = password
        self.id = id

    #SET
    def setUser(self, user):
        self.user = user

    def setPassword(self, password):
        self.password = password

    def setId(self, id):
        self.id = id

    #GET
    def getUser(self):
        return self.user

    def getPassword(self):
        return self.password

    def getId(self):
        return self.id    