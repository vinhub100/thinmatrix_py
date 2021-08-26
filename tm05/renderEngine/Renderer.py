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
        glDrawElements(GL_TRIANGLES, np.int32(model.getVertexCount()), GL_UNSIGNED_INT, None) 
        glDisableVertexAttribArray(0)
        glBindVertexArray(0)
