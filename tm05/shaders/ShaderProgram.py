from OpenGL.GL import *
import OpenGL.GL.shaders

class ShaderProgram():
    programID = None
    vertexShaderID = None
    fragmentShaderID = None

    def __init__(self, vertexFile, fragmentFile) -> None:
        vertexShader = self.loadShader(vertexFile)
        fragmentShader = self.loadShader(fragmentFile)
        self.vertexShaderID = OpenGL.GL.shaders.compileShader(vertexShader, GL_VERTEX_SHADER)
        self.fragmentShaderID = OpenGL.GL.shaders.compileShader(fragmentShader, GL_FRAGMENT_SHADER)
        self.programID = OpenGL.GL.shaders.compileProgram(self.vertexShaderID, self.fragmentShaderID)
        self.bindAttributes()

    def bindAttributes(self):
        return

    def bindAttribute(self, attribute, variableName):
        glBindAttribLocation(self.programID, attribute, variableName)
        return

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
    

