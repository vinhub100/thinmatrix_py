from models.TexturedModel import TexturedModel
from entities.Entity import Entity
from shaders.StaticShader import StaticShader
from renderEngine.Renderer import Renderer

class MasterRenderer:

    shader = None
    renderer = None

    entities = None

    def __init__(self) -> None:
        self.shader = StaticShader()
        self.renderer = Renderer(self.shader)
        self.entities = {}
        

    def render(self, sun, camera):
        self.renderer.prepare()
        self.shader.start()
        self.shader.loadLight(sun)
        self.shader.loadViewMatrix(camera)
        self.renderer.render(self.entities)
        self.shader.stop()
        self.entities.clear()
    
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
        self.shader.cleanUp()