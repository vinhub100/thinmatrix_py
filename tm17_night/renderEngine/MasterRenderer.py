from terrains.Terrain import Terrain
from OpenGL.GL import *
import pyrr
from models.TexturedModel import TexturedModel
from entities.Entity import Entity
from shaders.StaticShader import StaticShader
from shaders.TerrainShader import TerrainShader
from renderEngine.EntityRenderer import EntityRenderer
from renderEngine.TerrainRenderer import TerrainRenderer

class MasterRenderer:

    FOV = 30
    NEAR_PLANE = 0.1
    FAR_PLANE = 1000

    SKYCOLOR_R = 0.0
    SKYCOLOR_G = 0.0
    SKYCOLOR_B = 0.0

    FOGCOLOR_R = 0.0
    FOGCOLOR_G = 0.0
    FOGCOLOR_B = 0.0

    projectionMatrix = None

    entities = None
    shader = None
    renderer = None

    terrains = None
    terrainShader = None
    terrainRenderer = None

    def __init__(self) -> None:
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        self.projectionMatrix = pyrr.matrix44.create_perspective_projection_matrix(self.FOV, 16/9, self.NEAR_PLANE, self.FAR_PLANE)
        self.shader = StaticShader()
        self.renderer = EntityRenderer(self.shader, self.projectionMatrix)
        self.terrainShader = TerrainShader()
        self.terrainRenderer = TerrainRenderer(self.terrainShader, self.projectionMatrix)
        self.entities = {}
        self.terrains = []
    
    def prepare(self):
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(self.SKYCOLOR_R,self.SKYCOLOR_G,self.SKYCOLOR_B,1.0)
        
    
    # def disableCulling(self):
    #     glDisable(GL_CULL_FACE)

    def render(self, sun, camera):
        self.prepare()

        self.terrainShader.start()
        self.terrainShader.loadFogColor(self.FOGCOLOR_R,self.FOGCOLOR_G,self.FOGCOLOR_B)
        self.terrainShader.loadLight(sun)
        self.terrainShader.loadViewMatrix(camera)
        self.terrainRenderer.render(self.terrains)
        self.terrainShader.stop()

        self.shader.start()
        self.shader.loadFogColor(self.FOGCOLOR_R,self.FOGCOLOR_G,self.FOGCOLOR_B)
        self.shader.loadLight(sun)
        self.shader.loadViewMatrix(camera)
        self.renderer.render(self.entities)
        self.shader.stop()

        self.entities.clear()
        self.terrains.clear()
    
    def processTerrain(self, terrain:Terrain):
        self.terrains.append(terrain)
    
    def processEntity(self, entity:Entity):
        entityModel:TexturedModel = entity.getModel()
        batch = self.entities.get(entityModel)
        if batch != None :
            batch.append(entity)
        else:
            newBatch = []
            newBatch.append(entity)
            self.entities[entityModel] = newBatch

    def cleanUp(self):
        self.terrainShader.cleanUp()
        self.shader.cleanUp()
