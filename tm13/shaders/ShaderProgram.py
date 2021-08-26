from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

class ShaderProgram():
    programID = None
    vertexShaderID = None
    fragmentShaderID = None

    def __init__(self, vertexFile, fragmentFile) -> None:
        vertexShader = self.loadShader(vertexFile)
        fragmentShader = self.loadShader(fragmentFile)
        self.programID = glCreateProgram()
        self.programID = glCreateProgram()
        self.vertexShaderID = OpenGL.GL.shaders.compileShader(vertexShader, GL_VERTEX_SHADER)
        self.fragmentShaderID = OpenGL.GL.shaders.compileShader(fragmentShader, GL_FRAGMENT_SHADER)
        
        glAttachShader(self.programID, self.vertexShaderID)
        glAttachShader(self.programID, self.fragmentShaderID)
        self.bindAttributes()
        glLinkProgram(self.programID)
        glValidateProgram(self.programID)
        self.getAllUniformLocations()
        
    
    def getAllUniformLocations(self):
        return

    def getUniformLocation(self, uniformName):
        return glGetUniformLocation(self.programID, uniformName)

    def bindAttributes(self):
        return

    def bindAttribute(self, attribute, variableName):
        glBindAttribLocation(self.programID, attribute, variableName)
        return
    
    def loadFloat(self, location, value):
        glUniform1f(location, np.float32(value))
    
    def loadVector(self, location, vector):
        glUniform3f(location, np.float32(vector[0]), np.float32(vector[1]), np.float32(vector[2]))

    def loadBoolean(self, location, value):
        toLoad = np.float32(0)
        if value:
            toLoad = np.float32(1)
        glUniform1f(location, toLoad)
    
    def loadMatrix(self, location, matrix):
        glUniformMatrix4fv(location, 1, GL_FALSE, matrix)

    def start(self):
        glUseProgram(self.programID)
        return
    
    def stop(self):
        glUseProgram(0)
        return
        
    def cleanUp(self):
        self.stop()
        glDetachShader(self.programID, self.vertexShaderID)
        glDetachShader(self.programID, self.fragmentShaderID)
        # glDeleteShader(self.vertexShaderID)
        # glDeleteShader(self.fragmentShaderID)
        glDeleteProgram(self.programID)
        return

    def loadShader(self, file):
        with open(file) as shaderFile:
            shaderSource = shaderFile.read()
        return str.encode(shaderSource)
    

