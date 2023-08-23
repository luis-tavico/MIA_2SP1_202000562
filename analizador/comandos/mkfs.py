import struct

class Mkfs:
    def __init__(self, id = "", type = "", fs = ""):
        self.id = id #45
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
    
    def pack_data(self):
        return struct.pack('45s', self.id.encode(), self.type.encode(), self.fs.encode())

    @classmethod
    def unpack_data(cls, data_bytes):
        id, type, fs = struct.unpack('45s', data_bytes)
        return cls(id.decode(), type.decode(), fs.decode())
    
    def getLength(self):
        return 45