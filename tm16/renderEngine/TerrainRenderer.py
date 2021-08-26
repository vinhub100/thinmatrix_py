import numpy as np
from OpenGL.GL import *
from toolbox.Maths import Maths
from shaders.TerrainShader import TerrainShader
from terrains.Terrain import Terrain



class TerrainRenderer:
    terrainShader:TerrainShader = None

    math = Maths()

    def __init__(self, shader, projectionMatrix) -> None:
        self.terrainShader = shader
        self.terrainShader.start()
        self.terrainShader.loadProjectionMatrix(projectionMatrix)
        self.terrainShader.stop()
    
    def render(self,terrains):
        for terrain in terrains:
            self.prepareTerrain(terrain)
            self.loadModelMatrix(terrain)

            glDrawElements(GL_TRIANGLES, np.int32(terrain.getModel().getVertexCount()), GL_UNSIGNED_INT, None) 

            self.unbindTexturedModel()

    
    def prepareTerrain(self, terrain:Terrain):
        rmodel = terrain.getModel()
        glBindVertexArray(rmodel.getVaoID())
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        glEnableVertexAttribArray(2)
        texture = terrain.getTexture()
        self.terrainShader.loadShineVariables(texture.getShineDamper(),texture.getReflectivity())
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, texture.getID())

    def unbindTexturedModel(self):
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)
        glDisableVertexAttribArray(2)
        glBindVertexArray(0)

    def loadModelMatrix(self, terrain:Terrain):
        transformationMatrix = self.math.createTransformationMatrix([terrain.getX(), 0 , terrain.getZ()], 0.0, 0.0, 0.0, 1.0)
        self.terrainShader.loadTransformationMatrix(transformationMatrix)

