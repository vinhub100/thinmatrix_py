from OpenGL.GL import *
import numpy as np
from .RawModel import RawModel

class Renderer:
    def prepare(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1,0.5,0,1)
        
    
    def render(self, model):
        glBindVertexArray(model.getVaoID())
        glEnableVertexAttribArray(0)
        glDrawArrays(GL_TRIANGLES, 0, np.int32(model.getVertexCount()))
        glDisableVertexAttribArray(0)
        glBindVertexArray(0)
