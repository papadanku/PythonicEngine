# GL-Graphics-Engine

My take on Coder Space's Python 3D Engine Series.

## Differences

- Code is from myself following Coder Space's video tutorial
- Included documentation on how the program's modules work

## Modules

Module | Description
-------|-------------
`camera.py` | Camera data
`light.py` | Sunlight data
`main.py` | Main application
`mesh.py` | Mesh material information
`model.py` | Models' rendering information
`scene_renderer.py` | Scene rendering information
`scene.py` | Accumulated scene objects
`shader_program.py` | Mesh shaders
`texture.py` | Raw texture data
`vao.py` | Vertex Array Objects
`vbo.py` | Vertex Buffer Objects

## Rendering Process
Step | Code | Description | Generated/Processed Data
-----|------|-------------|-------------------------
0 | `def __init__()`| Create OpenGL information | OpenGL version • Window information
1 | `self.light = Light()` | Create sunlight data | Color • Orientation • Matrix
2 | `self.camera = Camera(self)` | Create camera data | Orientation • Matrices
3 | `self.mesh = Mesh(self)` | Create all mesh data | VBO • Shaders • VAO • Textures
4 | `self.scene = Scene(self)` | Accumulate objects in scene | `uniform` data for each objects' instance
5 | `self.scene_renderer = SceneRenderer(self)` | Render accumulated objects in the scene

## Notes

- Use literals to initialize data, such as `[]`
  - Constructor initialization, such as `list()`, changes how data's stored
- For each mesh, create *one* shared set of VBO, VAO, and shader programs
  - Change each mesh instance's attributes through `uniform` attributes
