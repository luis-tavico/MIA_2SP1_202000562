import struct
from datetime import datetime

from analizador.comandos.partition import Partition 

class Mbr:
    def __init__(self, tamano = 0, fecha_creacion = 0, dsk_signature = 0, fit = "B"):
        self.tamano = tamano
        self.fecha_creacion = fecha_creacion
        #self.fecha_creacion = int(round(fecha_creacion.timestamp()))
        self.dsk_signature = dsk_signature
        self.fit = fit
        self.partitions = [Partition(), Partition(), Partition(), Partition()]


    #SET
    def setTamano(self, tamano):
        self.tamano = tamano

    def setFecha_creacion(self, fecha_creacion):
        self.fecha_creacion = int(round(fecha_creacion.timestamp()))

    def setDsk_signature(self, dsk_signature):
        self.dsk_signature = dsk_signature

    def setFit(self, fit):
        self.fit = fit

    #GET
    def getTamano(self):
        return self.tamano

    def getFecha_creacion(self):
        return datetime.fromtimestamp(self.fecha_creacion)

    def getDsk_signature(self):
        return self.dsk_signature

    def getFit(self):
        return self.fit
    
    def getPartitions(self):
        return self.partitions
    
    #Empaquetar_Desempaquetar
    def pack_data(self):
        return struct.pack('iqic', self.tamano, self.fecha_creacion, self.dsk_signature, self.fit.encode())
    
    @classmethod
    def unpack_data(cls, data_bytes):
        tamano, fecha_creacion, dsk_signature, fit = struct.unpack('iqic', data_bytes)
        return cls(tamano, fecha_creacion, dsk_signature, fit.decode())
    
    def getLength(self):
        return struct.calcsize('iqic')

'''
from datetime import datetime
curr_dt = datetime.now()
timestamp = int(round(curr_dt.timestamp()))

mbr = Mbr(1, timestamp, 2, "F")
pack = mbr.pack_data()
print(pack)
unpack = mbr.unpack_data(pack)
print(unpack)
print(mbr.getLength())
#date = unpack.getFecha_creacion()
#timestamp_datetime = datetime.fromtimestamp(date)
#print(timestamp_datetime)

#for partition in unpack.getPartitions():
#    print(partition.getPart_name())
'''