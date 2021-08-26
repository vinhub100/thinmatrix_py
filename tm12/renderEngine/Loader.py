from OpenGL.GL import *
import numpy as np
from PIL import Image
from models.RawModel import RawModel

class Loader:
    vaos = []
    vbos = []
    textures = []

    def loadToVAO(self, positions,textureCoords, normals, indices):
        vaoID = self.createVAO()
        self.bindIndicesBuffer(indices)
        self.storeDataInAttributeList(0, 3, positions)
        self.storeDataInAttributeList(1, 2, textureCoords)
        self.storeDataInAttributeList(2, 3, normals)
        self.unbindVAO()
        return RawModel(vaoID, len(indices))
    
    def loadTexture(self, file):
        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)

        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        image = Image.open(file)
        # image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = image.convert("RGBA").tobytes()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
        self.textures.append(texture)
        return texture

    # cleanUp() - THERE IS A HUGE MISTAKE WITH THIS FUNCTION 
    def cleanUp(self):
        for va in self.vaos:
            glDeleteVertexArrays(1,va)
        for vb in self.vbos:
            glDeleteBuffers(1,vb)
        for texture in self.textures:
            glDeleteTextures(texture)

    def createVAO(self):
        vaoID = glGenVertexArrays(1)
        self.vaos.append(vaoID)
        glBindVertexArray(vaoID)
        return vaoID

    def storeDataInAttributeList(self, attributeNumber,coordinateSize, data):
        vboID = glGenBuffers(1)
        self.vbos.append(vboID)
        glBindBuffer(GL_ARRAY_BUFFER, vboID)
        buffer = np.array(data, dtype=np.float32)
        glBufferData(GL_ARRAY_BUFFER, buffer, GL_STATIC_DRAW)
        glVertexAttribPointer(attributeNumber, coordinateSize, GL_FLOAT, False, 0, 0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def unbindVAO(self):
        glBindVertexArray(0)
    
    def bindIndicesBuffer(self, indices):
        vboID = glGenBuffers(1)
        self.vbos.append(vboID)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vboID)
        buffer = np.array(indices, dtype=np.int32)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, buffer, GL_STATIC_DRAW)
