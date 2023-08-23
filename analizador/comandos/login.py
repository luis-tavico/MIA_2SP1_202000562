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
            
    def pack_data(self):
        return struct.pack('45s', self.id.encode(), self.type.encode(), self.fs.encode())

    @classmethod
    def unpack_data(cls, data_bytes):
        id, type, fs = struct.unpack('45s', data_bytes)
        return cls(id.decode(), type.decode(), fs.decode())
    
    def getLength(self):
        return 45