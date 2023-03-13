
"""
This module processes an application's scene objects
"""


# Import application modules
from model import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = list()
        self.load()
        # SkyBox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # Floor
        n, s = 20, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

        # Columns
        for i in range(9):
            add(Cube(app, pos=(15, i * s, -9 + i), tex_id=2))
            add(Cube(app, pos=(15, i * s, 5 - i), tex_id=2))

        # Cat
        add(Cat(app, pos=(0, -1, -10)))

        # Moving cube
        self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=1)
        add(self.moving_cube)

    def update(self):
        self.moving_cube.rot.xyz = self.app.time