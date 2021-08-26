from OpenGL.GL import *
import numpy as np
from .RawModel import RawModel

class Loader:
    vaos = []
    vbos = []

    def loadToVAO(self, positions):
        vaoID = self.createVAO()
        self.storeDataInAttributeList(0, positions)
        self.unbindVAO()
        return RawModel(vaoID, len(positions)/3)

    def cleanUp(self):
        for va in self.vaos:
            glDeleteVertexArrays(va)
        for vb in self.vbos:
            glDeleteBuffers(vb)

    def createVAO(self):
        vaoID = glGenVertexArrays(1)
        self.vaos.append(vaoID)
        glBindVertexArray(vaoID)
        return vaoID

    def storeDataInAttributeList(self, attributeNumber, data):
        vboID = glGenBuffers(1)
        self.vbos.append(vboID)
        glBindBuffer(GL_ARRAY_BUFFER, vboID)
        buffer = np.array(data, dtype=np.float32)
        glBufferData(GL_ARRAY_BUFFER, buffer, GL_STATIC_DRAW)
        glVertexAttribPointer(attributeNumber, 3, GL_FLOAT, False, 0, 0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def unbindVAO(self):
        glBindVertexArray(0)
