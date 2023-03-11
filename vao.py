
"""
This module processes an application's Vertex Array Objects (VAOs)
"""

# Import application modules
from shader_program import ShaderProgram
from vbo import VBO


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = dict()

        # Generate a Cube VAO for a specified shader program
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cube'])

        # Generate a Cat VAO for a specified shader program
        self.vaos['cat'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat'])

        # Generate a SkyBox VAO for a specified shader program
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox'])

        # Generate an advanced SkyBox VAO for a specified shader program
        self.vaos['advanced_skybox'] = self.get_vao(
            program=self.program.programs['advanced_skybox'],
            vbo=self.vbo.vbos['advanced_skybox'])

    # Converts a Vertex Buffer Object (VBO) to a Vertex Array Object (VAO)
    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()