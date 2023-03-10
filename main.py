
"""
This module initializes the main graphics application
"""

# Import Python modules
import moderngl as mgl
import pygame as pg
import sys

# Import application modules
from camera import Camera
from model import *

class GraphicsEngine():
    def __init__(self, win_size=(1600, 900)):
        # Initialize PyGame modules
        pg.init()
        # Initialize window size
        self.WIN_SIZE = win_size
        # Set OpenGL attributes
        # NOTE: This application uses OpenGL 3.3 Core
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # Create OpenGL context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # Detect and use existing OpenGL context
        # NOTE: Contexts provides render settings for functions such as depth testing, culling, etc.
        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # Create an object to help track time
        self.clock = pg.time.Clock()
        self.time = 0
        # Camera
        self.camera = Camera(self)
        # Scene
        self.scene = Cube(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # Clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        # Render scene
        self.scene.render()
        # Swap buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.render()
            self.clock.tick(60)

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
