import struct

class Data:
    def __init__(self, b_name, b_inodo):
        self.b_name = b_name
        self.b_inodo = b_inodo

    #SET
    def setName(self, b_name):
        self.b_name = b_name

    def setInodo(self, b_inodo):
        self.b_inodo = b_inodo

    #GET
    def getName(self):
        return self.b_name

    def getInodo(self):
        return self.b_inodo
    
   #Empaquetar_Desempaquetar
    def pack_data(self):
        return struct.pack('12si', self.b_name.encode(), self.b_inodo)
    
    @classmethod
    def unpack_data(cls, data_bytes):
        b_name, b_inodo = struct.unpack('12si', data_bytes)
        return cls(b_name.decode(), b_inodo)
    
    def getLength(self):
        return struct.calcsize('12si')
    

data = Data("name_file", 1)
pack = data.pack_data()
print(pack)
unpack = data.unpack_data(pack)
print(unpack)
print(data.getLength())
#date = unpack.getFecha_creacion()
#timestamp_datetime = datetime.fromtimestamp(date)
#print(timestamp_datetime)