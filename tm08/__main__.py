from entities.Camera import Camera
from entities.Entity import Entity
from shaders.StaticShader import StaticShader
from renderEngine.Renderer import Renderer
from models.TexturedModel import TexturedModel
from textures.ModelTexture import ModelTexture
from models.RawModel import RawModel
from renderEngine.Loader import Loader
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

    vertices = [-0.5, 0.5, -0.5,
                -0.5, -0.5, -0.5,
                0.5, -0.5, -0.5,
                0.5, 0.5, -0.5,

                -0.5, 0.5, 0.5,
                -0.5, -0.5, 0.5,
                0.5, -0.5, 0.5,
                0.5, 0.5, 0.5,

                0.5, 0.5, -0.5,
                0.5, -0.5, -0.5,
                0.5, -0.5, 0.5,
                0.5, 0.5, 0.5,

                -0.5, 0.5, -0.5,
                -0.5, -0.5, -0.5,
                -0.5, -0.5, 0.5,
                -0.5, 0.5, 0.5,

                -0.5, 0.5, 0.5,
                -0.5, 0.5, -0.5,
                0.5, 0.5, -0.5,
                0.5, 0.5, 0.5,

                -0.5, -0.5, 0.5,
                -0.5, -0.5, -0.5,
                0.5, -0.5, -0.5,
                0.5, -0.5, 0.5]

    indces = [0, 1, 3,
              3, 1, 2,
              4, 5, 7,
              7, 5, 6,
              8, 9, 11,
              11, 9, 10,
              12, 13, 15,
              15, 13, 14,
              16, 17, 19,
              19, 17, 18,
              20, 21, 23,
              23, 21, 22]

    texCoords = [0, 0,
                 0, 1,
                 1, 1,
                 1, 0,
                 0, 0,
                 0, 1,
                 1, 1,
                 1, 0,
                 0, 0,
                 0, 1,
                 1, 1,
                 1, 0,
                 0, 0,
                 0, 1,
                 1, 1,
                 1, 0,
                 0, 0,
                 0, 1,
                 1, 1,
                 1, 0,
                 0, 0,
                 0, 1,
                 1, 1,
                 1, 0]

    model = loader.loadToVAO(vertices, texCoords, indces)
    texture = ModelTexture(loader.loadTexture("res/sparrow.png"))
    texturedModel = TexturedModel(model, texture)

    entity = Entity(texturedModel, [0, 0, -2], 0, 0, 0, 1)
    entity2 = Entity(texturedModel, [1.0, 0.5, -1], 0, 0, 0, 0.15)

    while not dm.close():
        entity.increaseRotatioin(0, 1, 2)
        entity2.increaseRotatioin(0, 0, 1)
        camera.move()
        renderer.prepare()
        shader.start()
        shader.loadViewMatrix(camera)
        renderer.render(entity, shader)
        renderer.render(entity2, shader)
        shader.stop()
        dm.updateDisplay()

    shader.cleanUp()
    loader.cleanUp()
    dm.closeDisplay()

