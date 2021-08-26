

class ModelTexture:

    textureID = None
    shineDamper = 10.0
    reflectivity = 1.0

    def __init__(self, id) -> None:
        self.textureID = id
    
    def getID(self):
        return self.textureID

    def setShineDamper(self, shinedamper):
        self.shineDamper = shinedamper
    
    def getShineDamper(self):
        return self.shineDamper
    
    def setReflectivity(self, reflectvity):
        self.reflectivity = reflectvity
    
    def getReflectivity(self):
        return self.reflectivity
    
    