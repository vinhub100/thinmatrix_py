from .Entity import Entity
from renderEngine.DisplayManager import DisplayManager
from math import sin, cos, radians
from terrains.Terrain import Terrain

class Player(Entity):
    RUN_SPEED = 20.0
    TURN_SPEED = 70.0
    GRAVITY = -50
    JUMP_POWER = 30

    TERRAIN_HEIGHT = 0.0

    currentSpeed = 0.0
    currentTurnSpeed = 0.0
    upwardsSpeed = 0.0

    inAir = False


    def __init__(self, model, position, rotX, rotY, rotZ, scale) -> None:
        super().__init__(model, position, rotX, rotY, rotZ, scale)
    
    def move(self, dm:DisplayManager, terrain:Terrain):
        super().increaseRotatioin(0, self.currentTurnSpeed * dm.getFrameTimeInSec(), 0)
        distance = self.currentSpeed * dm.getFrameTimeInSec()
        dx = distance * sin(radians(super().getRotY()))
        dz = distance * cos(radians(super().getRotY()))
        super().increasePosition(dx, 0, -dz)
        self.upwardsSpeed += self.GRAVITY * dm.getFrameTimeInSec()
        super().increasePosition(0, self.upwardsSpeed * dm.getFrameTimeInSec(), 0)
        position = super().getPosition()
        terrainHeight = terrain.getHeightOfTerrain(position[0],position[2]) 
        if(position[1]<terrainHeight):
            self.upwardsSpeed = 0
            self.inAir = False
            super().setPosition([position[0], terrainHeight, position[2]])
        # print(position)
        
    def jump(self):
        if not self.inAir:
            self.upwardsSpeed = self.JUMP_POWER
            self.inAir = True

        

