#version 440 core

in vec2 pass_textureCoords;
in vec3 surfaceNormal;
in vec3 toLightVector;
in vec3 toCameraVector;
in float visibility;

out vec4 out_Colour;

uniform sampler2D textureSampler;
uniform vec3 lightColor;
uniform float shineDamper;
uniform float reflectivity;
uniform vec3 skyColor;

void main(void){
    vec3 unitNormal = normalize(surfaceNormal);
    vec3 unitLightVector = normalize(toLightVector);

    float nDotL = dot(unitNormal,unitLightVector);
    float brightness = max(nDotL, 0.4);
    vec3 diffuse = brightness * lightColor;

    vec3 unitVectorToCamera = normalize(toCameraVector);
    vec3 lightDirection = - unitLightVector;
    vec3 reflectedLightDirection = reflect(lightDirection, unitNormal);

    float specularFactor = dot(reflectedLightDirection, unitVectorToCamera);
    specularFactor = max(specularFactor, 0.0);
    float dampedFactor = pow(specularFactor,shineDamper);
    vec3 finalSpecular = dampedFactor * reflectivity * lightColor;

    vec4 textureColor = texture(textureSampler, pass_textureCoords);
    if(textureColor.a < 0.5){
        discard;
    }

    out_Colour = vec4(diffuse,1.0) * textureColor + vec4(finalSpecular, 0.0);
    out_Colour = mix(vec4(skyColor,1.0),out_Colour,visibility);
}
