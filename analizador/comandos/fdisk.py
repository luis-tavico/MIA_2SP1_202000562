import struct

class Fdisk:
    def __init__(self, size = 0, path = "", name = "",  unit = "K", type = "P", fit = "WF", delete = "", add = 0):
        self.size = str(size) #12
        self.path = path #45
        self.name = name #15
        self.unit = unit #2
        self.type = type #2
        self.fit = fit #3
        self.delete = delete #5
        self.add = str(add) #12

    #SET
    def setSize(self, size):
        self.size = size

    def setPath(self, path):
        self.path = path

    def setName(self, name):
        self.name = name

    def setUnit(self, unit):
        self.unit = unit

    def setType(self, type):
        self.type = type

    def setFit(self, fit):
        self.fit = fit

    def setDelete(self, delete):
        self.delete = delete

    def setAdd(self, add):
        self.add = add

    #GET
    def getSize(self):
        return self.size

    def getPath(self):
        return self.path

    def getName(self):
        return self.name

    def getUnit(self):
        return self.unit

    def getType(self):
        return self.type

    def getFit(self):
        return self.fit

    def getDelete(self):
        return self.delete

    def getAdd(self):
        return self.add
    
    def pack_data(self):
        return struct.pack('12s45s15s2s2s3s5s12s', self.size.encode(), self.path.encode(), self.name.encode(), self.unit.encode(), self.type.encode(), self.fit.encode(), self.delete.encode(), self.add.encode())

    @classmethod
    def unpack_data(cls, data_bytes):
        size, path, name,  unit, type, fit, delete, add = struct.unpack('12s45s15s2s2s3s5s12s', data_bytes)
        return cls(size.decode(), path.decode(), name.decode(),  unit.decode(), type.decode(), fit.decode(), delete.decode(), add.decode())
    
    def getLength(self):
        return 96