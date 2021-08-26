
class TexturedModel:
    rawModel = None
    texture = None

    def __init__(self, model, texture) -> None:
        self.rawModel = model
        self.texture = texture
    
    def getRawModel(self):
        return self.rawModel
    
    def getTexture(self):
        return self.texture
