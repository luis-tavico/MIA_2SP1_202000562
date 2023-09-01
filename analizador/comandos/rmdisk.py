import os
import struct

class Rmdisk:
    def __init__(self, path = ""):
        self.path = path
        self.errors = 0
    
    def setPath(self, path):
        self.path = path.replace("user", "luis_tavico").replace('"', "")
        if (not os.path.exists(self.path)):
            print("¡Error! el disco no existe.")
            self.errors += 1

    def getPath(self):
        return self.path

    def deleteDisk(self):
        r = input(f'¿Desea eliminar el disco {self.path} (s/n) ')
        if (r == 's'): 
            os.remove(self.path)
            print("¡Disco eliminado!")