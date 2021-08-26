import glfw

class Camera:
    position =[0, 0, 0]
    pitch, yaw, roll = 0, 0, 0
    left, right, forward, backward = False, False, False, False

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
            self.position[0] -= 0.1
        if self.right:
            self.position[0] += 0.1
        if self.forward:
            self.position[2] -= 0.1
        if self.backward:
            self.position[2] += 0.1

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
