import struct

class Mkdisk:
    def __init__(self, size = 0, path = "", fit = "FF", unit = "M"):
        self.size = size
        self.path = path
        self.fit = fit
        self.unit = unit
        self.errors = 0

    #SET
    def setSize(self, size):
        if (size > 0):
            self.size = size
        else:
            self.errors += 1
            print("¡Error! el valor del parametro 'size' debe ser mayor a 0.")

    def setPath(self, path):
        self.path = path
    
    def setFit(self, fit):
        if (fit == "BF"):
            self.fit = fit
        elif (fit == "FF"):
            self.fit = fit
        elif (fit == "WF"):
            self.fit = fit
        else:
            self.errors += 1
            print("¡Error! el valor del parametro 'fit' debe ser 'BF', 'FF' o 'WF'.")

    def setUnit(self, unit):
        if (unit == 'K'):
            self.unit = unit
        elif (unit == 'M'):
            self.unit = unit
        else:
            self.errors += 1
            print("¡Error! el valor del parametro 'unit' debe ser 'K' o 'M'.")

    '''
    def setSizePartition(self, size):
        if self.partition1 == 0:
            self.partition1 = size
        elif self.partition2 == 0:
            self.partition2 = size
        elif self.partition3 == 0:
            self.partition3 = size
        elif self.partition4 == 0:
            self.partition4 = size
    '''

    #GET
    def getSize(self):
        return self.size
    
    def getPath(self):
        return self.path
    
    def getFit(self):
        return self.fit
    
    def getUnit(self):
        return self.unit
    
    '''
    def getPartitionFree(self):
        if self.partition1 == 0 :
            return 76
        elif self.partition2 == 0:
            return self.partition1
        elif self.partition3 == 0:
            return self.partition2
        elif self.partition4 == 0:
            return self.partition3
        else:
            return None
    '''
    
    '''
    def pack_data(self):
        return struct.pack('q50s2siiii', self.size, self.path.encode(), self.unit.encode(), self.partition1, self.partition2, self.partition3, self.partition4)

    @classmethod
    def unpack_data(cls, data_bytes):
        size, path, fit, unit = struct.unpack('q50s2siiii', data_bytes)
        return cls(size, path.decode(), fit, unit.decode())
    
    def getLength(self):
        return 76
    '''