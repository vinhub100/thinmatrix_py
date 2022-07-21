from shaders.ShaderProgram import ShaderProgram
from toolbox.Maths import Maths

maths = Maths()

class TerrainShader(ShaderProgram):

    VERTEX_FILE = "tm23/shaders/terrainVertexShader.vs"
    FRAGMENT_FILE = "tm23/shaders/terrainFragmentShader.fs"

    location_transformationMatrix = None
    location_projectionMatrix = None
    location_viewMatrix = None
    location_lightPosition = None
    location_lightColor = None
    location_shineDamper = None
    location_reflectivity = None
    location_skyColor = None
    location_backgroundTexture = None
    location_rTexture = None
    location_gTexture = None
    location_bTexture = None
    location_blendMap = None

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
        self.location_skyColor = super().getUniformLocation("skyColor")
        self.location_backgroundTexture = super().getUniformLocation("backgroundTexture")
        self.location_rTexture = super().getUniformLocation("rTexture")
        self.location_gTexture = super().getUniformLocation("gTexture")
        self.location_bTexture = super().getUniformLocation("bTexture")
        self.location_blendMap = super().getUniformLocation("blendMap")
    
    def connectTextureUnits(self):
        super().loadInt(self.location_backgroundTexture, 0)
        super().loadInt(self.location_rTexture, 1)
        super().loadInt(self.location_gTexture, 2)
        super().loadInt(self.location_bTexture, 3)
        super().loadInt(self.location_blendMap, 4)

    def loadFogColor(self,r,g,b):
        super().loadVector(self.location_skyColor,[r,g,b])
     

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
