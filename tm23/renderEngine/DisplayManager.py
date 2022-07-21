import time
import glfw
from OpenGL.GL import *


class DisplayManager :
    def __init__(self) -> None:
        self.display = None
        self.window = None

        self.lastFrameTime = 0.0
        self.delta = 0.0
        
    def resizeCB(self,win, width, height):
        glViewport(0,0,width,height)

    def createDisplay(self):
        if not glfw.init():
            raise Exception("glfw can not be initialized!")
        

        # creating the window
        self.display = glfw.get_primary_monitor()
        self.window = glfw.create_window(1280, 720, "ThinMatrix", self.display, None)
        # check if window was created
        if not self.window:
            glfw.terminate()
            raise Exception("glfw window can not be created!")

        # set window's position
        # glfw.set_window_pos(self.window, 400, 200)

        glfw.set_window_size_callback(self.window, self.resizeCB)

        # make the context current
        glfw.make_context_current(self.window)

        glfw.set_input_mode(self.window, glfw.CURSOR, glfw.CURSOR_DISABLED)

        self.lastFrameTime = time.time()


    def updateDisplay(self):
        glfw.poll_events()
        glfw.swap_buffers(self.window)

        currentFrameTime = time.time()
        self.delta = currentFrameTime - self.lastFrameTime
        self.lastFrameTime = currentFrameTime


    def closeDisplay(self):
        glfw.terminate()

    def close(self):
        return glfw.window_should_close(self.window)
    
    def connectToCamera(self, camera):
        glfw.set_key_callback(self.window, camera.kbMove)
        glfw.set_cursor_pos_callback(self.window,camera.mouseMove)
        glfw.set_scroll_callback(self.window, camera.mouseScrollCB)
        glfw.set_mouse_button_callback(self.window, camera.mouseBtnClickCB)
    
    def getFrameTimeInSec(self):
        return self.delta
    
