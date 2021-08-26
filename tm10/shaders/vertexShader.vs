#version 440 core

in vec3 position;
in vec2 textureCoords;

out vec2 pass_textureCoords;

uniform mat4 transformationMatrix;
uniform mat4 projectionMatrix;
uniform mat4 viewMatrix;

void main(void){
    // gl_Position = vec4(position,1.0);
    gl_Position = (projectionMatrix * viewMatrix * transformationMatrix * vec4(position,1.0)) + vec4(0.0,-0.5,0.0,1.0);
    pass_textureCoords = textureCoords;
}
