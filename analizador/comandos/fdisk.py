import os
import struct

class Fdisk:
    def __init__(self, size = 0, path = "", name = "",  unit = "K", type = "P", fit = "WF", delete = "", add = 0):
        self.size = size
        self.path = path
        self.name = name
        self.unit = unit
        self.type = type
        self.fit = fit
        self.delete = delete
        self.add = add
        self.username = os.getlogin()
        self.errors = 0

    #SET
    def setSize(self, size):
        if (size > 0):
            self.size = size
        else:
            self.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("El valor del parametro 'size' debe ser mayor a 0."))

    def setPath(self, path):
        self.path = path.replace("user", self.username).replace('"', "")
        if not (os.path.exists(self.path)): 
            self.errors += 1  
            print("\033[91m<<Error>> {}\033[00m" .format("Disco no encontrado."))
    

    def setName(self, name):
        self.name = name

    def setUnit(self, unit):
        if (unit.lower() == "b"):
            self.unit = unit
        elif (unit.lower() == "k"):
            self.unit = unit
        elif (unit.lower() == "m"):
            self.unit = unit
        else:
            self.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("El valor del parametro 'unit' debe ser 'B', 'K' o 'M'."))

    def setType(self, type):
        if (type.lower() == "p"):
            self.type = type
        elif (type.lower() == "e"):
            self.type = type
        elif (type.lower() == "l"):
            self.type = type
        else:
            self.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("El valor del parametro 'type' debe ser 'P', 'E' o 'L'."))

    def setFit(self, fit):
        if (fit.lower() == "bf"):
            self.fit = fit
        elif (fit.lower() == "ff"):
            self.fit = fit
        elif (fit.lower() == "wf"):
            self.fit = fit
        else:
            self.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("El valor del parametro 'fit' debe ser 'BF', 'FF' o 'WF'."))

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