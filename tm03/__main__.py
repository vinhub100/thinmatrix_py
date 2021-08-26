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

    vertices = [-0.5,0.5,0,
                -0.5,-0.5,0,
                0.5,-0.5,0,
                0.5,0.5,0 ]
    
    indces = [0, 1, 3, 3, 1, 2]
    
    model = loader.loadToVAO(vertices, indces)

    while not dm.close():
        renderer.prepare()
        renderer.render(model)
        dm.updateDisplay()
    loader.cleanUp()
    dm.closeDisplay()

