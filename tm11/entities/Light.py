
class Light:

    position = [0.0,0.0,0.0]
    color = [0.0,0.0,0.0]

    def __init__(self, position, color) -> None:
        self.position = position
        self.color = color
    
    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position
    
    def getColor(self):
        return self.color
    
    def setPosition(self, color):
        self.color = color
    
    