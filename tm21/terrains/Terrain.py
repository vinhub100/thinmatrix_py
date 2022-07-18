
import pyrr
from PIL import Image
from numpy import asarray, array

from models.RawModel import RawModel
from textures.TerrainTexturePack import TerrainTexturePack
from textures.TerrainTexture import TerrainTexture
from renderEngine.Loader import Loader

class Terrain:
    SIZE:float = 800.0
    MAX_HEIGHT:float = 30.0
    MAX_PIXEL_COLOR:float = 256.0
    VERTEX_COUNT:int = 0.0
    x = None
    z = None
    model:RawModel = None
    texturePack:TerrainTexturePack = None
    blendMap:TerrainTexture = None

    def __init__(self, gridX:int, gridZ:int, loader:Loader, texturePack:TerrainTexturePack, blendMap:TerrainTexture, heightMap:str) -> None:
        self.texturePack = texturePack
        self.blendMap = blendMap
        self.x = gridX * self.SIZE
        self.z = gridZ * self.SIZE
        self.model = self.generateTerrain(loader, heightMap)
    

    def getX(self):
        return self.x
    
    def getZ(self):
        return self.z

    def getModel(self):
        return self.model
    
    def getTerrainTexturePack(self) -> TerrainTexturePack:
        return self.texturePack
    
    def getBlendMap(self) -> TerrainTexture:
        return self.blendMap

    def generateTerrain(self,loader:Loader, heightMap:str) -> RawModel:

        print(heightMap)
        try:
            image = Image.open('res/heightmap256.png')
        except Exception as e:
            print('No Height Map Loaded')
        
        self.VERTEX_COUNT = image.height

        count = self.VERTEX_COUNT ** 2
        vertices = [0.0] * (count * 3)
        normals = [0.0] * (count * 3)
        textureCoords = [0.0] * (count * 2)
        indices = [0] * (6 * (self.VERTEX_COUNT-1) ** 2)

        vertexPointer = 0

        for i in range(0, self.VERTEX_COUNT,1):
            for j in range(0, self.VERTEX_COUNT,1):
                vertices[vertexPointer*3] = float(j)/(float(self.VERTEX_COUNT)-1)*self.SIZE
                vertices[vertexPointer*3+1] = self.getHeight(j,i,image=image)
                vertices[vertexPointer*3+2] = float(i)/(float(self.VERTEX_COUNT)-1)*self.SIZE
                normal = self.calculateNormal(j,i,image=image)
                normals[vertexPointer*3] = normal[0]
                normals[vertexPointer*3+1] = normal[1]
                normals[vertexPointer*3+2] = normal[2]
                textureCoords[vertexPointer*2] = float(j)/(float(self.VERTEX_COUNT)-1)
                textureCoords[vertexPointer*2+1] = float(i)/(float(self.VERTEX_COUNT)-1)
                vertexPointer = vertexPointer+1
        
        pointer = 0
        for gz in range(0,self.VERTEX_COUNT-1,1):
            for gx in range(0,self.VERTEX_COUNT-1,1):
                topLeft = (gz*self.VERTEX_COUNT)+gx
                topRight = topLeft + 1
                bottomLeft = ((gz+1)*self.VERTEX_COUNT)+gx
                bottomRight = bottomLeft + 1
                
                indices[pointer] = topLeft
                pointer = pointer + 1
                indices[pointer] = bottomLeft
                pointer = pointer + 1
                indices[pointer] = topRight
                pointer = pointer + 1
                indices[pointer] = topRight
                pointer = pointer + 1
                indices[pointer] = bottomLeft
                pointer = pointer + 1
                indices[pointer] = bottomRight
                pointer = pointer + 1

        return loader.loadToVAO(vertices,textureCoords,normals,indices)
    

    def calculateNormal(self, x:int, y:int, image:Image.Image):
        heightL = self.getHeight(x-1,y,image=image)
        heightR = self.getHeight(x+1,y,image=image)
        heightD = self.getHeight(x,y-1,image=image)
        heightU = self.getHeight(x,y+1,image=image)
        normal = array([heightL-heightR, 2.0, heightD-heightU])
        return pyrr.vector.normalise(normal)

    def getHeight(self, x:int, y:int, image:Image.Image):
        if(x < 0 or x >= image.height or y < 0 or y >= image.height):
            return 0.0
        height = image.getpixel((x,y))[0]
        height -= self.MAX_PIXEL_COLOR / 2.0
        height /= self.MAX_PIXEL_COLOR / 2.0
        height *= self.MAX_HEIGHT
        return height
    
