
class Entity:
    model = None
    position = [0.0, 0.0, 0.0]
    rotX, rotY, rotZ = 0.0, 0.0, 0.0
    scale = 0.0

    def __init__(self, model, position, rotX, rotY, rotZ, scale) -> None:
        self.model = model
        self.position = position
        self.rotX = rotX
        self.rotY = rotY
        self.rotZ = rotZ
        self.scale = scale
    
    def setModel(self, model):
        self.model = model
    
    def getModel(self):
        return self.model
    
    def setPosition(self, position):
        self.position = position
    
    def getPosition(self):
        return self.position
    
    def setRotX(self, rotX):
        self.rotX = rotX
    
    def getRotX(self):
        return self.rotX
    
    def setRotY(self, rotY):
        self.rotY = rotY
    
    def getRotY(self):
        return self.rotY
    
    def setRotZ(self, rotZ):
        self.rotZ = rotZ
    
    def getRotZ(self):
        return self.rotZ

    def setScale(self, scale):
        self.scale = scale
    
    def getScale(self):
        return self.scale
    
    def increasePosition(self, dx, dy, dz):
        self.position[0] += dx
        self.position[1] += dy
        self.position[2] += dz
    
    def increaseRotatioin(self, dx, dy, dz):
        self.rotX += dx
        self.rotY += dy
        self.rotZ += dz
