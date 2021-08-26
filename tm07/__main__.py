import sys
sys.path.append(".")
import glfw
from OpenGL.GL import *
from renderEngine.DisplayManager import DisplayManager
from renderEngine.Loader import Loader
from models.RawModel import RawModel
from textures.ModelTexture import ModelTexture
from models.TexturedModel import TexturedModel
from renderEngine.Renderer import Renderer
from shaders.StaticShader import StaticShader

if __name__ == "__main__":
    dm = DisplayManager()
    dm.createDisplay()
    
    loader = Loader()
    renderer = Renderer()
    shader = StaticShader()

    vertices = [-0.3,0.5,0,
                -0.3,-0.5,0,
                0.3,-0.5,0,
                0.3,0.5,0 ]
    
    indces = [0, 1, 3, 3, 1, 2]

    texCoords = [0, 0, 0, 1, 1, 1, 1, 0]
    
    model = loader.loadToVAO(vertices, texCoords, indces)
    texture = ModelTexture(loader.loadTexture("res/sparrow.png"))
    texturedModel = TexturedModel(model, texture)


    while not dm.close():
        renderer.prepare()
        shader.start()
        renderer.render(texturedModel)
        shader.stop()
        dm.updateDisplay()
    
    shader.cleanUp()
    loader.cleanUp()
    dm.closeDisplay()

