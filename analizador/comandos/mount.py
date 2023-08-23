import struct

class Rmdisk:
    def __init__(self, path = "", name = ""):
        self.path = path #45
        self.name = name #15

    #SET
    def setPath(self, path):
        self.path = path

    def setName(self, name):
        self.name = name

    #GET
    def getPath(self):
        return self.path

    def getName(self):
        return self.name
    
    def pack_data(self):
        return struct.pack('45s15s', self.path.encode(), self.name.encode())

    @classmethod
    def unpack_data(cls, data_bytes):
        path, name = struct.unpack('45s15s', data_bytes)
        return cls(path.decode(), name.decode())
    
    def getLength(self):
        return 60