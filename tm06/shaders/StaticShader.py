from .ShaderProgram import ShaderProgram

class StaticShader(ShaderProgram):

    VERTEX_FILE = "tm06/shaders/vertexShader.vs"
    FRAGMENT_FILE = "tm06/shaders/fragmentShader.fs"

    def __init__(self) -> None:
        super().__init__(self.VERTEX_FILE, self.FRAGMENT_FILE)
    
    def bindAttributes(self):
        super().bindAttribute(0, "position")
        super().bindAttribute(1, "textureCoords")
