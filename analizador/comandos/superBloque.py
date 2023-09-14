import struct
from datetime import datetime

class SuperBloque:
    def __init__(self, filesystem_type = 0, inodes_count = 0, blocks_count = 0, free_blocks_count = 0, free_indoes_count = 0, mtime = 0, umtime = 0, mnt_count = 0, magic = 0, inode_s = 0, block_s = 0, firts_ino = 0, first_bio = 0, bm_inode_start = 0, bm_block_start = 0, inode_start = 0, block_start = 0):
        self.filesystem_type = filesystem_type
        self.inodes_count = inodes_count
        self.bloccks_count = blocks_count
        self.free_blocks_count = free_blocks_count
        self.free_indoes_count = free_indoes_count
        self.mtime = mtime
        self.umtime = umtime
        self.mnt_count = mnt_count
        self.magic = magic
        self.inode_s = inode_s
        self.block_s = block_s
        self.firts_ino = firts_ino
        self.first_bio = first_bio
        self.bm_inode_start = bm_inode_start
        self.bm_block_start = bm_block_start
        self.inode_start = inode_start
        self.block_start = block_start


    #SET
    def setFilesystem_type(self, filesystem_type):
        self.filesystem_type = filesystem_type

    def setInodes_count(self, inodes_count):
        self.inodes_count = inodes_count

    def setBlocks_count(self, blocks_count):
        self.blocks_count = blocks_count

    def setFree_blocks_count(self, free_blocks_count):
        self.free_blocks_count = free_blocks_count

    def setFree_indoes_count(self, free_indoes_count):
        self.free_indoes_count = free_indoes_count

    def setMtime(self, mtime):
        self.mtime = int(round(mtime.timestamp()))

    def setUmtime(self, umtime):
        self.umtime = int(round(umtime.timestamp()))

    def setMnt_count(self, mnt_count):
        self.mnt_count = mnt_count

    def setMagic(self, magic):
        self.magic = magic

    def setInode_s(self, inode_s):
        self.inode_s = inode_s

    def setBlock_s(self, block_s):
        self.block_s = block_s

    def setFirts_ino(self, firts_ino):
        self.firts_ino = firts_ino

    def setFirst_bio(self, first_bio):
        self.first_bio = first_bio

    def setBm_inode_start(self, bm_inode_start):
        self.bm_inode_start = bm_inode_start

    def setBm_block_start(self, bm_block_start):
        self.bm_block_start = bm_block_start

    def setInode_start(self, inode_start):
        self.inode_start = inode_start

    def setBlock_start(self, block_start):
        self.block_start = block_start

    #GET
    def getFilesystem_type(self):
        return self.filesystem_type

    def getInodes_count(self):
        return self.inodes_count

    def getBlocks_count(self):
        return self.blocks_count

    def getFree_blocks_count(self):
        return self.free_blocks_count

    def getFree_indoes_count(self):
        return self.free_indoes_count

    def getMtime(self):
        return datetime.fromtimestamp(self.mtime)

    def getUmtime(self):
        return datetime.fromtimestamp(self.umtime)

    def getMnt_count(self):
        return self.mnt_count

    def getMagic(self):
        return self.magic

    def getInode_s(self):
        return self.inode_s

    def getBlock_s(self):
        return self.block_s

    def getFirts_ino(self):
        return self.firts_ino

    def getFirst_bio(self):
        return self.first_bio

    def getBm_inode_start(self):
        return self.bm_inode_start

    def getBm_block_start(self):
        return self.bm_block_start

    def getInode_start(self):
        return self.inode_start

    def getBlock_start(self):
        return self.block_start
    
    #Empaquetar_Desempaquetar
    def pack_data(self):
        return struct.pack('iiiiiqqiiiiiiiiii', self.filesystem_type, self.inodes_count, self.bloccks_count, self.free_blocks_count, self.free_indoes_count, self.mtime, self.umtime, self.mnt_count, self.magic, self.inode_s, self.block_s, self.firts_ino, self.first_bio, self.bm_inode_start, self.bm_block_start, self.inode_start, self.block_start)
    
    @classmethod
    def unpack_data(cls, data_bytes):
        filesystem_type, inodes_count, blocks_count, free_blocks_count, free_indoes_count, mtime, umtime, mnt_count, magic, inode_s, block_s, firts_ino, first_bio, bm_inode_start, bm_block_start, inode_start, block_start = struct.unpack('iiiiiqqiiiiiiiiii', data_bytes)
        return cls(filesystem_type, inodes_count, blocks_count, free_blocks_count, free_indoes_count, mtime, umtime, mnt_count, magic, inode_s, block_s, firts_ino, first_bio, bm_inode_start, bm_block_start, inode_start, block_start)
    
    def getLength(self):
        return struct.calcsize('iiiiiqqiiiiiiiiii')
    
'''
from datetime import datetime
curr_dt = datetime.now()

super_bloque = SuperBloque(1, 2, 3, 4, 5, 0, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
super_bloque.setMtime(curr_dt)
super_bloque.setUmtime(curr_dt)
pack = super_bloque.pack_data()
print(pack)
unpack = super_bloque.unpack_data(pack)
print(unpack)
print(super_bloque.getLength())
#date = unpack.getFecha_creacion()
#timestamp_datetime = datetime.fromtimestamp(date)
#print(timestamp_datetime)
'''