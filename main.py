
"""
This module initializes the main graphics application
"""

# Import Python modules
import pygame as pg
import moderngl as mgl
import sys

# Import application modules
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
        self.ctx = mgl.create_context()
        # Create an object to help track time
        self.clock = pg.time.Clock()
        # Scene
        self.scene = Triangle(self)

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

    def run(self):
        while True:
            self.check_events()
            self.render()
            self.clock.tick(60)

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
