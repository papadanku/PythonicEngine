
"""
This module generates and destroys an application's shader programs
"""

class ShaderProgram:
    def __init__(self, ctx):
        self.ctx = ctx
        self.programs = dict()
        self.programs['default'] = self.get_program('default')

    def get_program(self, shader_program_name):
        # Get the vertex shader source code
        with open(f'shaders/{shader_program_name}.vert') as file:
            vertex_shader = file.read()

        # Get the fragment shader source code
        with open(f'shaders/{shader_program_name}.frag') as file:
            fragment_shader = file.read()

        # Compile the vertex and fragment shader to the application
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    def destroy(self):
        # Release program data from memory
        [program.release() for program in self.programs.values()]