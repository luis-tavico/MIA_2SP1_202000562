class Copy:
    def __init__(self, path = "", destino = ""):
        self.path = path
        self.destino = destino

    #SET
    def setPath(self, path):
        self.path = path.replace("user", "luis_tavico").replace('"', "")

    def setDestino(self, destino):
        self.destino = destino.replace("user", "luis_tavico").replace('"', "")

    #GET
    def getPath(self):
        return self.path
    
    def getDestino(self):
        return self.destino