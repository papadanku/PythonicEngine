# GL-Graphics-Engine

My take on Coder Space's Python 3D Engine Series.

## Changes

- Code is from myself following Coder Space's tutorial
- Various notes from information I learned from the tutorial
- Shader coding style

## Modules

Module | Description | Generated Data
-------|-------------|---------------
`camera.py` | Camera data | Orientation • Matrices
`light.py` | Sunlight data | Color • Orientation • Matrix
`main.py` | Main application
`mesh.py` | Mesh material information | VBOs • Shaders • VAOs • Textures
`model.py` | Models' rendering information | `uniform` attributes for meshes
`scene_renderer.py` | Scene rendering information
`scene.py` | Accumulated scene objects
`shader_program.py` | Mesh shaders
`texture.py` | Raw texture data
`vao.py` | Vertex Array Objects
`vbo.py` | Vertex Buffer Objects