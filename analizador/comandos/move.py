class Move:
    def __init__(self, path = "", destino = ""):
        self.path = path
        self.destino = destino

    #SET
    def setPath(self, path):
        self.path = path

    def setDestino(self, destino):
        self.destino = destino

    #GET
    def getPath(self):
        return self.path
    
    def getDestino(self):
        return self.destino