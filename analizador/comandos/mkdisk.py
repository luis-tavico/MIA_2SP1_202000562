import os

class Mkdisk:
    def __init__(self, size = 0, path = "", fit = "FF", unit = "M"):
        self.size = size
        self.path = path
        self.fit = fit
        self.unit = unit
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
        if not(os.path.exists(self.path)):
            carpetas = os.path.dirname(self.path)
            if not(os.path.exists(carpetas)):
                os.makedirs(carpetas)
        else:
            self.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("El disco ya existe."))
    
    def setFit(self, fit):
        if (fit == "BF"):
            self.fit = fit
        elif (fit == "FF"):
            self.fit = fit
        elif (fit == "WF"):
            self.fit = fit
        else:
            self.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("El valor del parametro 'fit' debe ser 'BF', 'FF' o 'WF'."))

    def setUnit(self, unit):
        if (unit == 'K'):
            self.unit = unit
        elif (unit == 'M'):
            self.unit = unit
        else:
            self.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("El valor del parametro 'unit' debe ser 'K' o 'M'."))

    #GET
    def getSize(self):
        return self.size
    
    def getPath(self):
        return self.path
    
    def getFit(self):
        return self.fit
    
    def getUnit(self):
        return self.unit