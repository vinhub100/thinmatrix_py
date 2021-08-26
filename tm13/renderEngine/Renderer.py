from OpenGL.GL import *
import numpy as np
import pyrr
from models.RawModel import RawModel
from models.TexturedModel import TexturedModel
from entities.Entity import Entity
from toolbox.Maths import Maths

class Renderer:

    FOV = 70
    NEAR_PLANE = 0.1
    FAR_PLANE = 1000

    projectionMatrix = None
    shader = None

    math = Maths()

    def __init__(self, shader) -> None:
        self.shader = shader
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        self.projectionMatrix = pyrr.matrix44.create_perspective_projection_matrix(self.FOV, 16/9, self.NEAR_PLANE, self.FAR_PLANE)
        self.shader.start()
        self.shader.loadProjectionMatrix(self.projectionMatrix)
        self.shader.stop()

    def prepare(self):
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0,0,0,1)
    
    def render(self, entities):
        for model in entities.keys():
            self.prepareTexturedModel(model)
            batch = entities.get(model)
            for entity in batch:
                self.prepareInstance(entity)
                glDrawElements(GL_TRIANGLES, np.int32(model.getRawModel().getVertexCount()), GL_UNSIGNED_INT, None) 
            self.unbindTexturedModel()

    def prepareTexturedModel(self, model:TexturedModel):
        rmodel = model.getRawModel()
        glBindVertexArray(rmodel.getVaoID())
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        glEnableVertexAttribArray(2)
        texture = model.getTexture()
        self.shader.loadShineVariables(texture.getShineDamper(),texture.getReflectivity())
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, model.getTexture().getID())

    def unbindTexturedModel(self):
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)
        glDisableVertexAttribArray(2)
        glBindVertexArray(0)

    def prepareInstance(self, entity:Entity):
        transformationMatrix = self.math.createTransformationMatrix(entity.getPosition(), entity.getRotX(), entity.getRotY(), entity.getRotZ(), entity.getScale())
        self.shader.loadTransformationMatrix(transformationMatrix)



    
    # def render(self, entity, shader):
    #     texturedModel = entity.getModel()
    #     model = texturedModel.getRawModel()
    #     glBindVertexArray(model.getVaoID())
    #     glEnableVertexAttribArray(0)
    #     glEnableVertexAttribArray(1)
    #     glEnableVertexAttribArray(2)

    #     transformationMatrix = self.math.createTransformationMatrix(entity.getPosition(), entity.getRotX(), entity.getRotY(), entity.getRotZ(), entity.getScale())
    #     shader.loadTransformationMatrix(transformationMatrix)

    #     texture = texturedModel.getTexture()
    #     shader.loadShineVariables(texture.getShineDamper(),texture.getReflectivity())
    #     glActiveTexture(GL_TEXTURE0)
    #     glBindTexture(GL_TEXTURE_2D, texturedModel.getTexture().getID())

    #     glDrawElements(GL_TRIANGLES, np.int32(model.getVertexCount()), GL_UNSIGNED_INT, None) 
    #     glDisableVertexAttribArray(0)
    #     glDisableVertexAttribArray(1)
    #     glDisableVertexAttribArray(2)
    #     glBindVertexArray(0)
