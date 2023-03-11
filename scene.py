
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

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        n, s, = 30, 3 # Number, step
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

    def render(self):
        for obj in self.objects:
            obj.render()