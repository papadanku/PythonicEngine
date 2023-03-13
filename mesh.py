
"""
This module gets the mesh's shader information (VAOs and textures)
"""

# Import application modules
from texture import Texture
from vao import VAO

class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app.ctx)
        self.texture = Texture(app)

    def destroy(self):
        self.vao.destroy()
        self.texture.destroy()
