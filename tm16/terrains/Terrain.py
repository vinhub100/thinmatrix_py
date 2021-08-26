
from models.RawModel import RawModel
from textures.ModelTexture import ModelTexture
from renderEngine.Loader import Loader

class Terrain:
    SIZE:float = 800.0
    VERTEX_COUNT:int = 128
    x = None
    z = None
    model:RawModel = None
    texture:ModelTexture = None

    def __init__(self, gridX:int, gridZ:int, loader:Loader, texture:ModelTexture) -> None:
        self.texture = texture
        self.x = gridX * self.SIZE
        self.z = gridZ * self.SIZE
        self.model = self.generateTerrain(loader)
    

    def getX(self):
        return self.x
    
    def getZ(self):
        return self.z

    def getModel(self):
        return self.model
    
    def getTexture(self):
        return self.texture

    def generateTerrain(self,loader:Loader) -> RawModel:
        count = self.VERTEX_COUNT ** 2
        vertices = [0.0] * (count * 3)
        normals = [0.0] * (count * 3)
        textureCoords = [0.0] * (count * 2)
        indices = [0] * (6 * (self.VERTEX_COUNT-1) ** 2)

        vertexPointer = 0

        for i in range(0, self.VERTEX_COUNT,1):
            for j in range(0, self.VERTEX_COUNT,1):
                vertices[vertexPointer*3] = float(j)/(float(self.VERTEX_COUNT)-1)*self.SIZE
                vertices[vertexPointer*3+1] = 0
                vertices[vertexPointer*3+2] = float(i)/(float(self.VERTEX_COUNT)-1)*self.SIZE
                normals[vertexPointer*3] = 0
                normals[vertexPointer*3+1] = 1
                normals[vertexPointer*3+2] = 0
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