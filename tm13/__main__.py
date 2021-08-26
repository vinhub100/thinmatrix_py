from entities.Camera import Camera
from entities.Entity import Entity
from entities.Light import Light
from shaders.StaticShader import StaticShader
from renderEngine.Renderer import Renderer
from renderEngine.MasterRenderer import MasterRenderer
from models.TexturedModel import TexturedModel
from textures.ModelTexture import ModelTexture
from models.RawModel import RawModel
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
    # renderer = Renderer(shader)
    mRenderer = MasterRenderer()
    camera = Camera()

    dm.connectKeyboardToCamera(camera)


    model = loadObjModel("res/dragon.obj", loader)
    texture = ModelTexture(loader.loadTexture("res/white256.png"))
    texture.setShineDamper(1000.0)
    texture.setReflectivity(100.0)
    texturedModel = TexturedModel(model, texture)

    # entity = Entity(texturedModel, [0, 0, -25], 0, 0, 0, 1)
    # entity2 = Entity(texturedModel, [1.0, 0.5, -1], 0, 0, 0, 0.15)

    allEntities = []
    for i in range(0,20,1):
        x = float(random.random() * 80 - 40)
        # y = float(random.random() * 20 - 10)
        y = float(-0.8)
        z = float(random.random() * - 150)
        tempEntity = Entity(texturedModel,[x,y,z],0.0, random.random() * 180.0, 0.0, 0.5)
        allEntities.append(tempEntity)


    light = Light([1, 10, -10], [1.0,0.5,0.0])

    # shader.start()
    # shader.loadLight(light)
    # shader.stop()

    while not dm.close():
        # entity.increaseRotatioin(0, 1, 0)
        # entity2.increaseRotatioin(0, 0, 1)
        camera.move()

        for enty in allEntities:
            mRenderer.processEntity(enty)
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

