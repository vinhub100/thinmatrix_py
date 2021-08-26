from OpenGL.GL import *
import numpy as np
import pyrr
from models.RawModel import RawModel
from toolbox.Maths import Maths

class Renderer:

    FOV = 70
    NEAR_PLANE = 0.1
    FAR_PLANE = 1000

    projectionMatrix = None

    math = Maths()

    def __init__(self, shader) -> None:
        self.projectionMatrix = pyrr.matrix44.create_perspective_projection_matrix(self.FOV, 16/9, self.NEAR_PLANE, self.FAR_PLANE)
        shader.start()
        shader.loadProjectionMatrix(self.projectionMatrix)
        shader.stop()

    def prepare(self):
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0,0,0,1)
        
    
    def render(self, entity, shader):
        texturedModel = entity.getModel()
        model = texturedModel.getRawModel()
        glBindVertexArray(model.getVaoID())
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        glEnableVertexAttribArray(2)

        transformationMatrix = self.math.createTransformationMatrix(entity.getPosition(), entity.getRotX(), entity.getRotY(), entity.getRotZ(), entity.getScale())
        shader.loadTransformationMatrix(transformationMatrix)

        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, texturedModel.getTexture().getID())
        glDrawElements(GL_TRIANGLES, np.int32(model.getVertexCount()), GL_UNSIGNED_INT, None) 
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)
        glDisableVertexAttribArray(2)
        glBindVertexArray(0)
