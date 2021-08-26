import glfw
from OpenGL.GL import *
from renderEngine.DisplayManager import DisplayManager
from renderEngine.Loader import Loader
from renderEngine.RawModel import RawModel
from renderEngine.Renderer import Renderer

if __name__ == "__main__":
    dm = DisplayManager()
    dm.createDisplay()
    
    loader = Loader()
    renderer = Renderer()

    vertices = [-0.5,0.5,0.5,
                -0.5,-0.5,0,
                1.5,-0.5,0,
                1.5,-0.5,0,
                0.5,0.5,0,
                -0.5,0.5,0.5 ]
    
    model = loader.loadToVAO(vertices)

    while not dm.close():
        renderer.prepare()
        renderer.render(model)
        dm.updateDisplay()
    loader.cleanUp()
    dm.closeDisplay()

