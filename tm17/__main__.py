# import sys
# sys.path.append(".")
from entities.Camera import Camera
from entities.Entity import Entity
from entities.Light import Light
from shaders.StaticShader import StaticShader
from renderEngine.EntityRenderer import EntityRenderer
from renderEngine.MasterRenderer import MasterRenderer
from models.TexturedModel import TexturedModel
from textures.ModelTexture import ModelTexture
from textures.TerrainTexture import TerrainTexture
from textures.TerrainTexturePack import TerrainTexturePack
from models.RawModel import RawModel
from terrains.Terrain import Terrain
from renderEngine.Loader import Loader
from renderEngine.OBJLoader import loadObjModel
from renderEngine.DisplayManager import DisplayManager
from OpenGL.GL import *
import glfw
import random


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


    grassModel = loadObjModel("res/grassModel.obj", loader)
    grassTexture = ModelTexture(loader.loadTexture("res/grassTexture.png"))
    grassTexture.setTransprency(True)
    grassTexture.setFakeLighting(True)
    # texture.setShineDamper(1000.0)
    # texture.setReflectivity(100.0)
    grass = TexturedModel(grassModel, grassTexture)

    treeModel = loadObjModel("res/tree.obj", loader)
    treeTexture = ModelTexture(loader.loadTexture("res/tree.png"))
    # texture.setShineDamper(1000.0)
    # texture.setReflectivity(100.0)
    tree = TexturedModel(treeModel, treeTexture)

    lowPolyTreeModel = loadObjModel("res/lowPolyTree.obj", loader)
    lowPolyTreeTexture = ModelTexture(loader.loadTexture("res/lowPolyTree.png"))
    # texture.setShineDamper(1000.0)
    # texture.setReflectivity(100.0)
    lowPolyTree = TexturedModel(lowPolyTreeModel, lowPolyTreeTexture)

    plantModel = loadObjModel("res/fern.obj", loader)
    plantTexture = ModelTexture(loader.loadTexture("res/fern.png"))
    # plantTexture.setShineDamper(1000.0)
    plantTexture.setTransprency(True)
    plantTexture.setFakeLighting(True)
    plantTexture.setReflectivity(0.0)
    plant = TexturedModel(plantModel, plantTexture)

    backgroundTexture = TerrainTexture(loader.loadTexture("res/grassy.png"))
    rTexture = TerrainTexture(loader.loadTexture("res/mud.png"))
    gTexture = TerrainTexture(loader.loadTexture("res/grassFlowers.png"))
    bTexture = TerrainTexture(loader.loadTexture("res/path.png"))

    texturePack = TerrainTexturePack(backgroundTexture,rTexture,gTexture,bTexture)
    blendMap = TerrainTexture(loader.loadTexture("res/blendMap.png"))

    terrain1 = Terrain(0,-1,loader,texturePack,blendMap)
    terrain2 = Terrain(-1,-1,loader,texturePack,blendMap)
    terrain3 = Terrain(0,0,loader,texturePack,blendMap)
    terrain4 = Terrain(-1,0,loader,texturePack,blendMap)

    # entity = Entity(texturedModel, [0, 0, -25], 0, 0, 0, 1)
    # entity2 = Entity(texturedModel, [1.0, 0.5, -1], 0, 0, 0, 0.15)

    grassField = []
    for i in range(0,100,1):
        x = float(random.random() * 400 - 200)
        # y = float(random.random() * 20 - 10)
        y = float(-0.75)
        z = float(random.random() * 400 - 200)
        tempGrass = Entity(grass,[x,y,z],0.0, random.random() * 180.0, 0.0, 1.4)
        grassField.append(tempGrass)

    trees = []
    for i in range(0,50,1):
        x = float(random.random() * 600 - 300)
        # y = float(random.random() * 20 - 10)
        y = float(-0.75)
        z = float(random.random() * 600 - 300)
        tempTree = Entity(tree,[x,y,z],0.0, random.random() * 180.0, 0.0, 8.0)
        trees.append(tempTree)

    polyTree = []
    for i in range(0,10,1):
        x = float(random.random() * 600 - 300)
        # y = float(random.random() * 20 - 10)
        y = float(-0.75)
        z = float(random.random() * 600 - 300)
        tempPolyTree = Entity(lowPolyTree,[x,y,z],0.0, random.random() * 180.0, 0.0, 0.8)
        polyTree.append(tempPolyTree)
    
    plants = []
    for i in range(0,50,1):
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

        for grs in grassField:
            mRenderer.processEntity(grs)
        
        for tre in trees:
            mRenderer.processEntity(tre)
        
        for plnt in plants:
            mRenderer.processEntity(plnt)
        
        for pTree in polyTree:
            mRenderer.processEntity(pTree)
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

