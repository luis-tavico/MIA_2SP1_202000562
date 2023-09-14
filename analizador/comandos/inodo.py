import struct
from datetime import datetime

class Inodo:
    def __init__(self, uid, gid, s, atime, ctime, mtime, block, type, perm):
        self.uid = uid
        self.gid = gid
        self.s = s
        self.atime = atime
        self.ctime = ctime
        self.mtime = mtime
        self.block = block
        self.type = type
        self.perm = perm
        
    #SET
    def setUid(self, uid):
        self.uid = uid

    def setGid(self, gid):
        self.gid = gid

    def setS(self, s):
        self.s = s

    def setAtime(self, atime):
        self.atime = atime

    def setCtime(self, ctime):
        self.ctime = ctime

    def setMtime(self, mtime):
        self.mtime = mtime

    def setBlock(self, block):
        self.block = block

    def setType(self, type):
        self.type = type

    def setPerm(self, perm):
        self.perm = perm

    #GET
    def getUid(self):
        return self.uid

    def getGid(self):
        return self.gid

    def getS(self):
        return self.s

    def getAtime(self):
        return self.atime

    def getCtime(self):
        return self.ctime

    def getMtime(self):
        return self.mtime

    def getBlock(self):
        return self.block

    def getType(self):
        return self.type

    def getPerm(self):
        return self.perm
    
    #Empaquetar_Desempaquetar
    def pack_data(self):
        return struct.pack('iiiqqqici', self.uid, self.gid, self.s, self.atime, self.ctime, self.mtime, self.block, self.type.encode(), self.perm)
    
    @classmethod
    def unpack_data(cls, data_bytes):
        uid, gid, s, atime, ctime, mtime, block, type, perm = struct.unpack('iiiqqqici', data_bytes)
        return cls(uid, gid, s, atime, ctime, mtime, block, type.decode(), perm)
    
    def getLength(self):
        return struct.calcsize('iiiqqqici')

'''
from datetime import datetime
curr_dt = datetime.now()
timestamp = int(round(curr_dt.timestamp()))

inodo = Inodo(1, 2, 3, timestamp, timestamp, timestamp, 4, 'F', 5)
pack = inodo.pack_data()
print(pack)
unpack = inodo.unpack_data(pack)
print(unpack)
print(inodo.getLength())
#date = unpack.getFecha_creacion()
#timestamp_datetime = datetime.fromtimestamp(date)
#print(timestamp_datetime)
'''