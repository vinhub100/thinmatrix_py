from shaders.ShaderProgram import ShaderProgram
from toolbox.Maths import Maths

maths = Maths()

class StaticShader(ShaderProgram):

    VERTEX_FILE = "tm23/shaders/vertexShader.vs"
    FRAGMENT_FILE = "tm23/shaders/fragmentShader.fs"

    location_transformationMatrix = None
    location_projectionMatrix = None
    location_viewMatrix = None
    location_lightPosition = None
    location_lightColor = None
    location_shineDamper = None
    location_reflectivity = None
    location_useFakeLight = None
    location_skyColor = None

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
        self.location_shineDamper = super().getUniformLocation("shineDamper")
        self.location_reflectivity = super().getUniformLocation("reflectivity")
        self.location_useFakeLight = super().getUniformLocation("useFakeLight")
        self.location_skyColor = super().getUniformLocation("skyColor")
    
    def loadFogColor(self,r,g,b):
        super().loadVector(self.location_skyColor,[r,g,b])
    
    def loadFakeLight(self, fakeLight:bool):
        super().loadBoolean(self.location_useFakeLight, fakeLight)

    def loadShineVariables(self, damper, reflectivity):
        super().loadFloat(self.location_reflectivity, reflectivity)
        super().loadFloat(self.location_shineDamper, damper)
    
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
