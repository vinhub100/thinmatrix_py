import glfw
from OpenGL.GL import *
from renderEngine.DisplayManager import DisplayManager

if __name__ == "__main__":
    dm = DisplayManager()
    dm.createDisplay()
    glClearColor(0, 1, 1, 1)
    while not dm.close():
        glClear(GL_COLOR_BUFFER_BIT)
        # do stuff heres
        dm.updateDisplay()
    dm.closeDisplay()

