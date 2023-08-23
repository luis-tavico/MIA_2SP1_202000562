import os
import struct

class Rmdisk:
    def __init__(self, path = ""):
        self.path = path
        self.errors = 0
    
    def setPath(self, path):
        if (os.path.exists(path)):
            self.path = path
        else:
            print("¡Error! el disco no existe.")
            self.errors += 1

    def getPath(self):
        return self.path

    def deleteDisk(self):
        r = input(f'¿Desea eliminar el disco {self.path} (s/n) ')
        if (r == 's'): 
            os.remove(self.path)
            print("¡Disco eliminado!")