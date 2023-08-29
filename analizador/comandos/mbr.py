import struct

from partition import Partition 

class Mbr:
    def __init__(self, tamano = None, fecha_creacion = None, dsk_signature = None, fit = None):
        self.tamano = tamano
        self.fecha_creacion = fecha_creacion
        self.dsk_signature = dsk_signature
        self.fit = fit
        self.partitions = [Partition("A", "B", "C", 123, 123, "partition1"), Partition("D", "E", "F", 123, 123, "partition2"), Partition("G", "H", "I", 123, 123, "partition3"), Partition("J", "K", "L", 123, 123, "partition4")]

    #SET
    def setTamano(self, tamano):
        self.tamano = tamano

    def setFecha_creacion(self, fecha_creacion):
        self.fecha_creacion = fecha_creacion

    def setDsk_signature(self, dsk_signature):
        self.dsk_signature = dsk_signature

    def setFit(self, fit):
        self.fit = fit

    #GET
    def getTamano(self):
        return self.tamano

    def getFecha_creacion(self):
        return self.fecha_creacion

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
        return 17


from datetime import datetime
curr_dt = datetime.now()
timestamp = int(round(curr_dt.timestamp()))

mbr = Mbr(3000000, timestamp, 430, "F")
pack = mbr.pack_data()
print(pack)
unpack = mbr.unpack_data(pack)
print(unpack)
#date = unpack.getFecha_creacion()
#timestamp_datetime = datetime.fromtimestamp(date)
#print(timestamp_datetime)

for partition in unpack.getPartitions():
    print(partition.getPart_name())