from OpenGL.raw.GL.VERSION.GL_2_0 import glGetUniformLocation
from shaders.ShaderProgram import ShaderProgram
from toolbox.Maths import Maths

maths = Maths()

class StaticShader(ShaderProgram):

    VERTEX_FILE = "tm11/shaders/vertexShader.vs"
    FRAGMENT_FILE = "tm11/shaders/fragmentShader.fs"

    location_transformationMatrix = None
    location_projectionMatrix = None
    location_viewMatrix = None
    location_lightPosition = None
    location_lightColor = None

    def __init__(self) -> None:
        super().__init__(self.VERTEX_FILE, self.FRAGMENT_FILE)
    
    def bindAttributes(self):
        super().bindAttribute(0, "position")
        super().bindAttribute(1, "textureCoords")
        super().bindAttribute(2, "normal")
    
    def getAllUniformLocations(self):
        super().getAllUniformLocations()
        self.location_transformationMatrix = super().getUniformLocation("transformationMatrix")
        # projectionMatrix
        self.location_projectionMatrix = super().getUniformLocation("projectionMatrix")
        self.location_viewMatrix = super().getUniformLocation("viewMatrix")
        self.location_lightPosition = super().getUniformLocation("lightPosition")
        self.location_lightColor = super().getUniformLocation("lightColor")
    
    def loadTransformationMatrix(self, matrix):
        super().loadMatrix(self.location_transformationMatrix, matrix)
    
    def loadLight(self, light):
        super().loadVector(self.location_lightPosition, light.getPosition())
        super().loadVector(self.location_lightColor, light.getColor())

    def loadProjectionMatrix(self, matrix):
        super().loadMatrix(self.location_projectionMatrix, matrix)
    
    def loadViewMatrix(self, camera):
        matrix = maths.createViewMatrix(camera)
        super().loadMatrix(self.location_viewMatrix, matrix)
