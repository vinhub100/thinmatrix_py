import numpy as np
from OpenGL.GL import *
from toolbox.Maths import Maths
from shaders.TerrainShader import TerrainShader
from terrains.Terrain import Terrain
from textures.TerrainTexturePack import TerrainTexturePack
from textures.TerrainTexture import TerrainTexture



class TerrainRenderer:
    terrainShader:TerrainShader = None

    math = Maths()

    def __init__(self, shader, projectionMatrix) -> None:
        self.terrainShader = shader
        self.terrainShader.start()
        self.terrainShader.loadProjectionMatrix(projectionMatrix)
        self.terrainShader.connectTextureUnits()
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
        self.bindTextures(terrain)
        self.terrainShader.loadShineVariables(1,0)
    
    def bindTextures(self,terrain:Terrain):
        texturePack:TerrainTexturePack = terrain.getTerrainTexturePack()
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, texturePack.getBackgroundTexture().getTextureID())
        glActiveTexture(GL_TEXTURE1)
        glBindTexture(GL_TEXTURE_2D, texturePack.getRTexture().getTextureID())
        glActiveTexture(GL_TEXTURE2)
        glBindTexture(GL_TEXTURE_2D, texturePack.getGTexture().getTextureID())
        glActiveTexture(GL_TEXTURE3)
        glBindTexture(GL_TEXTURE_2D, texturePack.getBTexture().getTextureID())
        glActiveTexture(GL_TEXTURE4)
        glBindTexture(GL_TEXTURE_2D, terrain.getBlendMap().getTextureID())
        

    def unbindTexturedModel(self):
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)
        glDisableVertexAttribArray(2)
        glBindVertexArray(0)

    def loadModelMatrix(self, terrain:Terrain):
        transformationMatrix = self.math.createTransformationMatrix([terrain.getX(), 0 , terrain.getZ()], 0.0, 0.0, 0.0, 1.0)
        self.terrainShader.loadTransformationMatrix(transformationMatrix)

