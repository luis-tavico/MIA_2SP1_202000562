import os
import struct

class Fdisk:
    def __init__(self, size = 0, path = "", name = "",  unit = "K"):
        self.size = size #8
        self.path = path #50
        self.name = name #15
        self.unit = unit #2
        self.errors = 0

    #SET
    def setSize(self, size):
        self.size = size

    def setPath(self, path):
        if os.path.exists(path):
            self.path = path
        else:
            self.errors += 1
            print("¡Error! disco no encontrado.")

    def setName(self, name):
        self.name = name

    def setUnit(self, unit):
        self.unit = unit

    #GET
    def getSize(self):
        return self.size

    def getPath(self):
        return self.path

    def getName(self):
        return self.name

    def getUnit(self):
        return self.unit
    
    def pack_data(self):
        return struct.pack('q50s15s2s', self.size, self.path.encode(), self.name.encode(), self.unit.encode())

    @classmethod
    def unpack_data(cls, data_bytes):
        size, path, name,  unit = struct.unpack('q50s15s2s', data_bytes)
        return cls(size, path.decode(), name.decode(),  unit.decode())
    
    def getLength(self):
        return 75