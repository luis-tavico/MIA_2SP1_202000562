import os
import struct

class Fdisk:
    def __init__(self, size = 0, path = "", name = "",  unit = "K", type = "", fit = "", delete = "", add = ""):
        self.size = size #8
        self.path = path #50
        self.name = name #15
        self.unit = unit #2
        self.type = type
        self.fit = fit
        self.delete = delete
        self.add = add
        self.errors = 0

    #SET
    def setSize(self, size):
        if (size > 0):
            self.size = size
        else:
            self.errors += 1
            print("¡Ocurrio un error al asignar valor al parametro 'size', el valor debe ser mayor a 0!")


    def setPath(self, path):
        if os.path.exists(path):
            self.path = path
        else:
            self.errors += 1
            print("¡Error! disco no encontrado.")

    def setName(self, name):
        self.name = name

    def setUnit(self, unit):
        if (unit == "B"):
            self.unit = unit
        elif (unit == "K"):
            self.unit = unit
        elif (unit == "M"):
            self.unit = unit
        else:
            self.errors += 1
            print("¡Error! el valor del parametro 'unit' debe ser 'B', 'K' o 'M'.")

    def setType(self, type):
        if (type == "P"):
            self.type = type
        elif (type == "E"):
            self.type = type
        elif (type == "L"):
            self.type = type
        else:
            self.errors += 1
            print("¡Error! el valor del parametro 'type' debe ser 'P', 'E' o 'L'.")

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


    def delete(self, delete):
        self.delete = delete

    def add(self, add):
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
    
    def pack_data(self):
        return struct.pack('q50s15s2s', self.size, self.path.encode(), self.name.encode(), self.unit.encode())

    @classmethod
    def unpack_data(cls, data_bytes):
        size, path, name,  unit = struct.unpack('q50s15s2s', data_bytes)
        return cls(size, path.decode(), name.decode(),  unit.decode())
    
    def getLength(self):
        return 75