from OpenGL.raw.GL.VERSION.GL_2_0 import glGetUniformLocation
from .ShaderProgram import ShaderProgram

class StaticShader(ShaderProgram):

    VERTEX_FILE = "tm07/shaders/vertexShader.vs"
    FRAGMENT_FILE = "tm07/shaders/fragmentShader.fs"

    location_transformationMatrix = None

    def __init__(self) -> None:
        super().__init__(self.VERTEX_FILE, self.FRAGMENT_FILE)
    
    def bindAttributes(self):
        super().bindAttribute(0, "position")
        super().bindAttribute(1, "textureCoords")
    
    def getAllUniformLocations(self):
        super().getAllUniformLocations()
        location_transformationMatrix = super().getUniformLocation("transformationMatrix")
    
    def loadTransformationMatrix(self, matrix):
        super().loadMatrix(self.location_transformationMatrix, matrix)
