from .ShaderProgram import ShaderProgram

class StaticShader(ShaderProgram):

    VERTEX_FILE = "tm05/shaders/vertexShader.glsl"
    FRAGMENT_FILE = "tm05/shaders/fragmentShader.glsl"

    def __init__(self) -> None:
        super().__init__(self.VERTEX_FILE, self.FRAGMENT_FILE)
    
    def bindAttributes(self):
        super().bindAttribute(0, "position")
        