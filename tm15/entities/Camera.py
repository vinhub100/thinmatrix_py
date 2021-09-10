import glfw
from math import radians, sin, cos

class Camera:
    position =[0, 2, 0]
    pitch, yaw, roll = 0, 0, 0
    left, right, forward, backward = False, False, False, False

    lastX, lastY = 640, 360
    mouseSensitivity = 0.25
    first_mouse = True

    def getPosition(self):
        return self.position
    
    def getPitch(self):
        return self.pitch
    
    def getYaw(self):
        return self.yaw

    def getRoll(self):
        return self.roll

    def move(self):
        if self.left:
            self.position[0] -= 0.5 * cos(radians(self.yaw))
            self.position[2] += 0.5 * sin(radians(self.yaw))
        if self.right:
            self.position[0] += 0.5 * cos(radians(self.yaw))
            self.position[2] -= 0.5 * sin(radians(self.yaw))
        if self.forward:
            self.position[0] -= 0.5 * sin(radians(self.yaw))
            self.position[2] -= 0.5 * cos(radians(self.yaw))
        if self.backward:
            self.position[0] += 0.5 * sin(radians(self.yaw))
            self.position[2] += 0.5 * cos(radians(self.yaw))

    def kbMove(self, window, key, scancode, action, mode):

        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(window, True)

        if key == glfw.KEY_W and action == glfw.PRESS:
            self.forward = True
        elif key == glfw.KEY_W and action == glfw.RELEASE:
            self.forward = False
        if key == glfw.KEY_S and action == glfw.PRESS:
            self.backward = True
        elif key == glfw.KEY_S and action == glfw.RELEASE:
            self.backward = False
        if key == glfw.KEY_A and action == glfw.PRESS:
            self.left = True
        elif key == glfw.KEY_A and action == glfw.RELEASE:
            self.left = False
        if key == glfw.KEY_D and action == glfw.PRESS:
            self.right = True
        elif key == glfw.KEY_D and action == glfw.RELEASE:
            self.right = False
    
    def mouseMove(self, window, xpos, ypos):
        if self.first_mouse:
            self.lastX = xpos
            self.lastY = ypos
            self.first_mouse = False
        
        xoffset = xpos - self.lastX
        yoffset = self.lastY - ypos

        self.lastX = xpos
        self.lastY = ypos

        xoffset *= self.mouseSensitivity
        # yoffset *= self.mouseSensitivity

        self.yaw += xoffset
        # self.pitch -= yoffset

        # self.position[0] = cos(radians(self.yaw)) * cos(radians(self.pitch))
        # # self.position[1] = 2
        # self.position[2] = sin(radians(self.yaw)) * cos(radians(self.pitch))
        


    
