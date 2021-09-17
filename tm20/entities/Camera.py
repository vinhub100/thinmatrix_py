import glfw
from math import radians, sin, cos
from entities.Player import Player

class Camera:

    position =[0, 5, 0]
    pitch, yaw, roll = 0, 0, 0
    left, right, forward, backward = False, False, False, False

    distanceFromPlayer = 50
    angleAroundPlayer = 0
    angleAbovePlayer = 0
    rightClick = False
    leftClick = False

    lastX, lastY = 0, 0
    mouseSensitivity = 0.1
    first_mouse = True

    player:Player = None
    
    def setPlayer(self, player:Player):
        self.player = player

    def getPosition(self):
        return self.position
    
    def getPitch(self):
        return self.pitch
    
    def getYaw(self):
        return self.yaw

    def getRoll(self):
        return self.roll

    def move(self):
        radPitch = radians(self.angleAbovePlayer)
        horizontalDistance = self.distanceFromPlayer * cos(radPitch)
        verticalDistance = self.distanceFromPlayer * sin(radPitch)
        theta = radians(-self.player.getRotY() + self.angleAroundPlayer)
        offsetX = horizontalDistance * sin(theta)
        offsetZ = horizontalDistance * cos(theta)
        self.position[0] = self.player.position[0] - offsetX
        self.position[1] =  verticalDistance
        self.position[2] = self.player.position[2] - offsetZ
        self.pitch = self.angleAbovePlayer
        self.yaw = 180-(self.player.getRotY() - self.angleAroundPlayer)


    def kbMove(self, window, key, scancode, action, mode):

        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(window, True)
        
        # if key == glfw.KEY_W and action == glfw.PRESS:
        #     self.forward = True
        # elif  key == glfw.KEY_W and action == glfw.RELEASE:
        #     self.forward = False

        # if key == glfw.KEY_S and action == glfw.PRESS:
        #     self.backward = True
        # elif key == glfw.KEY_S and action == glfw.RELEASE:
        #     self.backward = False

        # if key == glfw.KEY_A and action == glfw.PRESS:
        #     self.left = True
        # elif key == glfw.KEY_A and action == glfw.RELEASE:
        #     self.left = False

        # if key == glfw.KEY_D and action == glfw.PRESS:
        #     self.right = True
        # elif key == glfw.KEY_D and action == glfw.RELEASE:
        #     self.right = False
        
        if key == glfw.KEY_UP and action == glfw.PRESS:
            self.player.currentSpeed = -self.player.RUN_SPEED
        elif key == glfw.KEY_UP and action == glfw.RELEASE:
            self.player.currentSpeed = 0
        
        if key == glfw.KEY_DOWN and action == glfw.PRESS:
            self.player.currentSpeed = self.player.RUN_SPEED
        elif key == glfw.KEY_DOWN and action == glfw.RELEASE:
            self.player.currentSpeed = 0
        
        if key == glfw.KEY_RIGHT and action == glfw.PRESS:
            self.player.currentTurnSpeed = self.player.TURN_SPEED
        elif key == glfw.KEY_RIGHT and action == glfw.RELEASE:
            self.player.currentTurnSpeed = 0
        
        if key == glfw.KEY_LEFT and action == glfw.PRESS:
            self.player.currentTurnSpeed = -self.player.TURN_SPEED
        elif key == glfw.KEY_LEFT and action == glfw.RELEASE:
            self.player.currentTurnSpeed = 0
        
        if key == glfw.KEY_SPACE and action == glfw.PRESS:
            self.player.jump()

    
    def mouseMove(self, window, xpos, ypos):
        if self.first_mouse:
            self.lastX = xpos
            self.lastY = ypos
            self.first_mouse = False
        
        xoffset = xpos - self.lastX
        yoffset = self.lastY - ypos

        self.lastX = xpos
        self.lastY = ypos

        if self.rightClick:
            yoffset *= self.mouseSensitivity
            self.angleAbovePlayer += yoffset
            if self.angleAbovePlayer < 0:
                self.angleAbovePlayer = 0
            elif self.angleAbovePlayer > 90:
                self.angleAbovePlayer = 90
            return

        if self.leftClick:
            xoffset *= self.mouseSensitivity
            self.angleAroundPlayer += xoffset
            return

        self.player.rotY += xoffset

        # self.position[0] = cos(radians(self.yaw)) * cos(radians(self.pitch))
        # # self.position[1] = 2
        # self.position[2] = sin(radians(self.yaw)) * cos(radians(self.pitch))
    
    def mouseBtnClickCB(self, window, button, action, mods):
        if button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.PRESS:
            self.rightClick = True
        elif button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.RELEASE:
            self.rightClick = False
        if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
            self.leftClick = True
        elif button == glfw.MOUSE_BUTTON_LEFT and action == glfw.RELEASE:
            self.leftClick = False

    def mouseScrollCB(self, window, xOffset, yOffset):
        self.distanceFromPlayer -= yOffset * 5
        if self.distanceFromPlayer < 0:
            self.distanceFromPlayer = 0


