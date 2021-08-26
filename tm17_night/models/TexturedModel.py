
class TexturedModel:
    rawModel = None
    texture = None
    hash = None

    def __init__(self, model, texture) -> None:
        self.rawModel = model
        self.texture = texture
        self.hash = hash(str(model.getVaoID()) + "-" + str(texture.getID()))
    
    def __eq__(self, o: object) -> bool:
        if self.getHash() == o.getHash():
            return True
        return False
    
    def __hash__(self) -> int:
        return self.hash
    
    def getRawModel(self):
        return self.rawModel
    
    def getTexture(self):
        return self.texture
    
    def getHash(self):
        return self.hash
