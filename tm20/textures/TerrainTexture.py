
class TerrainTexture:

    textureID:int = None

    def __init__(self, textureID) -> None:
        self.textureID = textureID
    
    def getTextureID(self):
        return self.textureID
    