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

    FOV = 60
    NEAR_PLANE = 0.1
    FAR_PLANE = 1000

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
        glClearColor(0,0.5,0.6,1)

    def render(self, sun, camera):
        self.prepare()

        self.terrainShader.start()
        self.terrainShader.loadLight(sun)
        self.terrainShader.loadViewMatrix(camera)
        self.terrainRenderer.render(self.terrains)
        self.terrainShader.stop()

        self.shader.start()
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
