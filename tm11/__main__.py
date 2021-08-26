from entities.Camera import Camera
from entities.Entity import Entity
from entities.Light import Light
from shaders.StaticShader import StaticShader
from renderEngine.Renderer import Renderer
from models.TexturedModel import TexturedModel
from textures.ModelTexture import ModelTexture
from models.RawModel import RawModel
from renderEngine.Loader import Loader
from renderEngine.OBJLoader import loadObjModel
from renderEngine.DisplayManager import DisplayManager
from OpenGL.GL import *
import glfw
import sys
sys.path.append(".")

if __name__ == "__main__":
    dm = DisplayManager()
    dm.createDisplay()

    loader = Loader()
    shader = StaticShader()
    renderer = Renderer(shader)
    camera = Camera()

    dm.connectKeyboardToCamera(camera)


    model = loadObjModel("res/dragon.obj", loader)
    texture = ModelTexture(loader.loadTexture("res/white256.png"))
    texturedModel = TexturedModel(model, texture)

    entity = Entity(texturedModel, [0, 0, -25], 0, 0, 0, 1)
    # entity2 = Entity(texturedModel, [1.0, 0.5, -1], 0, 0, 0, 0.15)

    light = Light([20,0,-10], [1.0,0.5,0.0])

    shader.start()
    shader.loadLight(light)
    shader.stop()

    

    while not dm.close():
        entity.increaseRotatioin(0, 1, 0)
        # entity2.increaseRotatioin(0, 0, 1)
        camera.move()
        renderer.prepare()
        shader.start()
        shader.loadViewMatrix(camera)
        renderer.render(entity, shader)
        # renderer.render(entity2, shader)
        shader.stop()
        dm.updateDisplay()

    shader.cleanUp()
    loader.cleanUp()
    dm.closeDisplay()

