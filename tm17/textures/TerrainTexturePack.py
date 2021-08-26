from textures.TerrainTexture import TerrainTexture

class TerrainTexturePack:

    backgroundTexture:TerrainTexture = None
    rTexture:TerrainTexture = None
    gTexture:TerrainTexture = None
    bTexture:TerrainTexture = None

    def __init__(self, backgroundTexture:TerrainTexture, rTexture:TerrainTexture, gTexture:TerrainTexture, bTexture:TerrainTexture) -> None:
        self.backgroundTexture = backgroundTexture
        self.rTexture = rTexture
        self.gTexture = gTexture
        self.bTexture = bTexture
    
    def getBackgroundTexture(self) -> TerrainTexture:
        return self.backgroundTexture
    
    def getRTexture(self) -> TerrainTexture:
        return self.rTexture
    
    def getGTexture(self) -> TerrainTexture:
        return self.gTexture
    
    def getBTexture(self) -> TerrainTexture:
        return self.bTexture
    
    