#version 420 core

in vec3 colour;
out vec4 out_Colour;

void main(void){
    out_Colour = vec4(colour,1.0);
}
