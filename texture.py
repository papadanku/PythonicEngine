
"""
This module processes an application's textures
"""

# Import Python modules
import pygame as pg


class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = dict()
        self.textures[0] = self.get_texture(path='textures/img.png')
        self.textures[1] = self.get_texture(path='textures/img_1.png')
        self.textures[2] = self.get_texture(path='textures/img_2.png')

    def get_texture(self, path):
        # NOTE: Flip the texture along the Y-axis because PyGame has a downward Y-axis
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]