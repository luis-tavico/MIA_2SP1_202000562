import struct

class Mkdisk:
    def __init__(self, size = 0, path = "", fit = "FF", unit = "M"):
        self.size = str(size) #12
        self.path = path #45
        self.fit = fit #3
        self.unit = unit #2
        self.errors = 0

    #SET
    def setSize(self, size):
        if (int(size) > 0):
            self.size = size
        else:
            self.errors += 1
            print("¡Ocurrio un error al asignar valor al parametro 'size', el valor debe ser mayor a 0!")

    def setPath(self, path):
        self.path = path

    def setFit(self, fit):
        self.fit = fit

    def setUnit(self, unit):
        self.unit = unit

    #GET
    def getSize(self):
        return self.size
    
    def getPath(self):
        return self.path
    
    def getFit(self):
        return self.fit
    
    def getUnit(self):
        return self.unit
    
    def pack_data(self):
        return struct.pack('12s45s3s2s', self.size.encode(), self.path.encode(), self.fit.encode(), self.unit.encode())

    @classmethod
    def unpack_data(cls, data_bytes):
        size, path, fit, unit = struct.unpack('12s45s3s2s', data_bytes)
        return cls(size.decode(), path.decode(), fit.decode(), unit.decode())
    
    def getLength(self):
        return 62