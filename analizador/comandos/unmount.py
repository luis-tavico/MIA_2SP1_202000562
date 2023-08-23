import struct

class Rmdisk:
    def __init__(self, id=""):
        self.id = id #12

    #SET
    def setId(self, id):
        self.id = id

    #GET
    def getId(self):
        return self.id

    def pack_data(self):
        return struct.pack('12s', self.id.encode())

    @classmethod
    def unpack_data(cls, data_bytes):
        id = struct.unpack('12s', data_bytes)
        return cls(id.decode())
    
    def getLength(self):
        return 12