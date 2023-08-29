import struct

class Mkdisk:
    def __init__(self, size = 0, path = "", fit = "", unit = "M", partition1 = 0, partition2 = 0, partition3 = 0, partition4 = 0):
        self.size = size
        self.path = path #50
        self.fit = fit
        self.unit = unit #2
        self.partition1 = partition1
        self.partition2 = partition2
        self.partition3 = partition3
        self.partition4 = partition4
        self.errors = 0

    #SET
    def setSize(self, size):
        if (size > 0):
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

    def setSizePartition(self, size):
        if self.partition1 == 0:
            self.partition1 = size
        elif self.partition2 == 0:
            self.partition2 = size
        elif self.partition3 == 0:
            self.partition3 = size
        elif self.partition4 == 0:
            self.partition4 = size

    #GET
    def getSize(self):
        return self.size
    
    def getPath(self):
        return self.path
    
    def getUnit(self):
        return self.unit
    
    def getSizePartition1(self):
        return self.partition1

    def getSizePartition2(self):
        return self.partition2

    def getSizePartition3(self):
        return self.partition3

    def getSizePartition4(self):
        return self.partition4
    
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
    
    def pack_data(self):
        return struct.pack('q50s2siiii', self.size, self.path.encode(), self.unit.encode(), self.partition1, self.partition2, self.partition3, self.partition4)

    @classmethod
    def unpack_data(cls, data_bytes):
        size, path, unit, partition1, partition2, partition3, partition4 = struct.unpack('q50s2siiii', data_bytes)
        return cls(size, path.decode(), unit.decode(), partition1, partition2, partition3, partition4)
    
    def getLength(self):
        return 76