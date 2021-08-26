from entities.Camera import Camera
from entities.Entity import Entity
from entities.Light import Light
from shaders.StaticShader import StaticShader
from renderEngine.EntityRenderer import EntityRenderer
from renderEngine.MasterRenderer import MasterRenderer
from models.TexturedModel import TexturedModel
from textures.ModelTexture import ModelTexture
from models.RawModel import RawModel
from terrains.Terrain import Terrain
from renderEngine.Loader import Loader
from renderEngine.OBJLoader import loadObjModel
from renderEngine.DisplayManager import DisplayManager
from OpenGL.GL import *
import glfw
import random
import sys
sys.path.append(".")

if __name__ == "__main__":
    dm = DisplayManager()
    dm.createDisplay()

    loader = Loader()
    # shader = StaticShader()
    # renderer = EntityRenderer(shader)
    mRenderer = MasterRenderer()
    camera = Camera()

    dm.connectKeyboardToCamera(camera)
    dm.connectMouseToCamera(camera)


    model = loadObjModel("res/grassModel.obj", loader)
    texture = ModelTexture(loader.loadTexture("res/grassTexture.png"))
    texture.setTransprency(True)
    texture.setFakeLighting(True)
    # texture.setShineDamper(1000.0)
    # texture.setReflectivity(100.0)
    texturedModel = TexturedModel(model, texture)

    treeModel = loadObjModel("res/tree.obj", loader)
    treeTexture = ModelTexture(loader.loadTexture("res/tree.png"))
    # texture.setShineDamper(1000.0)
    # texture.setReflectivity(100.0)
    tree = TexturedModel(treeModel, treeTexture)

    plantModel = loadObjModel("res/fern.obj", loader)
    plantTexture = ModelTexture(loader.loadTexture("res/fern.png"))
    # plantTexture.setShineDamper(1000.0)
    plantTexture.setTransprency(True)
    plantTexture.setFakeLighting(True)
    plantTexture.setReflectivity(0.0)
    plant = TexturedModel(plantModel, plantTexture)

    terrainTexture = ModelTexture(loader.loadTexture("res/grass.png"))
    terrainTexture2 = ModelTexture(loader.loadTexture("res/grass2.png"))
    terrainTexture3 = ModelTexture(loader.loadTexture("res/grass3.png"))
    terrainTexture4 = ModelTexture(loader.loadTexture("res/grass4.png"))
    terrain1 = Terrain(0,-1,loader,terrainTexture)
    terrain2 = Terrain(-1,-1,loader,terrainTexture)
    terrain3 = Terrain(0,0,loader,terrainTexture)
    terrain4 = Terrain(-1,0,loader,terrainTexture)

    # entity = Entity(texturedModel, [0, 0, -25], 0, 0, 0, 1)
    # entity2 = Entity(texturedModel, [1.0, 0.5, -1], 0, 0, 0, 0.15)

    allEntities = []
    for i in range(0,100,1):
        x = float(random.random() * 300 - 150)
        # y = float(random.random() * 20 - 10)
        y = float(-0.75)
        z = float(random.random() * 300 - 150)
        tempEntity = Entity(texturedModel,[x,y,z],0.0, random.random() * 180.0, 0.0, 1)
        allEntities.append(tempEntity)

    trees = []
    for i in range(0,50,1):
        x = float(random.random() * 400 - 200)
        # y = float(random.random() * 20 - 10)
        y = float(-0.75)
        z = float(random.random() * 400 - 200)
        tempTree = Entity(tree,[x,y,z],0.0, random.random() * 180.0, 0.0, 5.0)
        trees.append(tempTree)
    
    plants = []
    for i in range(0,20,1):
        x = float(random.random() * 200 - 100)
        # y = float(random.random() * 20 - 10)
        y = float(-0.75)
        z = float(random.random() * 200 - 100)
        tempPlant = Entity(plant,[x,y,z],0.0, random.random() * 180.0, 0.0, 0.6)
        plants.append(tempPlant)

    light = Light([1000, 2000, 100], [1.0,1.0,1.0])

    # shader.start()
    # shader.loadLight(light)
    # shader.stop()

    while not dm.close():
        # entity.increaseRotatioin(0, 1, 0)
        # entity2.increaseRotatioin(0, 0, 1)
        camera.move()

        mRenderer.processTerrain(terrain1)
        mRenderer.processTerrain(terrain2)
        mRenderer.processTerrain(terrain3)
        mRenderer.processTerrain(terrain4)

        for enty in allEntities:
            mRenderer.processEntity(enty)
        
        for tre in trees:
            mRenderer.processEntity(tre)
        
        for plnt in plants:
            mRenderer.processEntity(plnt)
        # renderer.prepare()
        # shader.start()
        # shader.loadViewMatrix(camera)
        # renderer.render(entity, shader)
        # renderer.render(entity2, shader)
        mRenderer.render(light, camera)
        # shader.stop()
        dm.updateDisplay()

    # shader.cleanUp()
    mRenderer.cleanUp()
    loader.cleanUp()
    dm.closeDisplay()

