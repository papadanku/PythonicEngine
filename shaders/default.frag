
#version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;
in vec4 shadowCoord;

struct Light
{
    vec3 position;
    vec3 Ia;
    vec3 Id;
    vec3 Is;
};

uniform Light light;
uniform sampler2D u_texture_0;
uniform vec3 camPos;
uniform sampler2DShadow shadowMap;
uniform vec2 u_resolution;

float lookup(float ox, float oy)
{
    vec2 pixelOffset = 1.0 / u_resolution;
    // NOTE: Multiply by shadowCoord.w due to GPU's perspective division!
    return textureProj(shadowMap, shadowCoord + vec4(vec2(ox, oy) * pixelOffset * shadowCoord.ww, 0.0, 0.0));
}

float getSoftShadowX16()
{
    float shadow;
    float swidth = 1.0;
    float endp = swidth * 1.5;
    for (float y = -endp; y <= endp; y += swidth)
    {
        for (float x = -endp; x <= endp; x += swidth) 
        {
            shadow += lookup(x, y);
        }
    }
    return shadow / 16.0;
}

float getShadow()
{
    float shadow = textureProj(shadowMap, shadowCoord);
    return shadow;
}

vec3 getLight(vec3 color)
{
    vec3 Normal = normalize(normal);

    // Ambient light
    vec3 ambient = light.Ia;

    // Diffuse light
    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0, dot(lightDir, Normal));
    vec3 diffuse = diff * light.Id;

    // Specular light
    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0), 32);
    vec3 specular = spec * light.Is;

    // float shadow = getShadow();
    float shadow = getSoftShadowX16();

    return color * (ambient + (diffuse + specular) * shadow);
}

void main()
{
    float gamma = 2.2;
    vec3 color = texture(u_texture_0, uv_0).rgb;
    color = pow(color, vec3(gamma));

    color = getLight(color);

    color = pow(color, 1.0 / vec3(gamma));
    fragColor = vec4(color, 1.0);
}