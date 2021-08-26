#version 440 core

in vec2 pass_textureCoords;
in vec3 surfaceNormal;
in vec3 toLightVector;

out vec4 out_Colour;

uniform sampler2D textureSampler;
uniform vec3 lightColor;

void main(void){
    vec3 unitNormal = normalize(surfaceNormal);
    vec3 unitLightVector = normalize(toLightVector);

    float nDotL = dot(unitNormal,unitLightVector);
    float brightness = max(nDotL, 0.4);
    vec3 diffuse = brightness * lightColor;

    out_Colour = vec4(diffuse,1.0) * texture(textureSampler, pass_textureCoords);
}
