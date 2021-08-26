from OpenGL.GL import *
import numpy as np
from models.RawModel import RawModel

class Renderer:
    def prepare(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1,0.5,0,1)
        
    
    def render(self, texturedModel):
        model = texturedModel.getRawModel()
        glBindVertexArray(model.getVaoID())
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, texturedModel.getTexture().getID())
        glDrawElements(GL_TRIANGLES, np.int32(model.getVertexCount()), GL_UNSIGNED_INT, None) 
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)
        glBindVertexArray(0)
