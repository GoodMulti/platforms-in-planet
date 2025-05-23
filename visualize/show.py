"""Display a simulation using pyglet 2.1."""

from __future__ import annotations

import math
import os

import pyglet
from pyglet.gl import (
    glEnable, glDisable, glBindTexture, glMatrixMode, glLoadIdentity,
    glTranslatef, glRotatef, glClearColor, GL_DEPTH_TEST,
    GL_PROJECTION, GL_MODELVIEW, GL_TRIANGLES
)
from pyglet import gl

from objects import Earth
from simulation import Simulation


class Show(pyglet.window.Window):
    """Simple viewer for a :class:`Simulation`."""

    def __init__(self, simulation: Simulation, texture_file: str = "earth.jpg") -> None:
        super().__init__(800, 600, "Simulation", resizable=True)
        self.simulation = simulation
        self.azimuth = 0.0
        self.elevation = 0.0
        self.distance = 3.0
        self.fps_display = pyglet.window.FPSDisplay(self)
        self.texture = None
        if os.path.exists(texture_file):
            self.texture = pyglet.image.load(texture_file).get_texture()
        gl.glClearColor(0, 0, 0, 1)
        self.sphere = self._create_sphere()

    def _create_sphere(self, radius: float = 1.0, slices: int = 40, stacks: int = 40):
        vertices = []
        tex = []
        indices = []
        for stack in range(stacks + 1):
            phi = math.pi * stack / stacks
            y = radius * math.cos(phi)
            r = radius * math.sin(phi)
            for slice in range(slices + 1):
                theta = 2 * math.pi * slice / slices
                x = r * math.cos(theta)
                z = r * math.sin(theta)
                vertices.extend([x, y, z])
                tex.extend([slice / slices, 1 - stack / stacks])
        for stack in range(stacks):
            for slice in range(slices):
                first = stack * (slices + 1) + slice
                second = first + slices + 1
                indices.extend([first, second, first + 1, second, second + 1, first + 1])
        vertex_list = pyglet.graphics.vertex_list_indexed(
            len(vertices) // 3,
            indices,
            ("v3f/static", vertices),
            ("t2f/static", tex),
        )
        return vertex_list

    def on_draw(self) -> None:
        self.clear()
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect = self.width / float(self.height)
        gl.gluPerspective(60.0, aspect, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -self.distance)
        glRotatef(self.elevation, 1, 0, 0)
        glRotatef(self.azimuth, 0, 1, 0)

        if self.texture:
            glEnable(self.texture.target)
            glBindTexture(self.texture.target, self.texture.id)
        else:
            gl.glColor3f(0.0, 0.2, 1.0)

        self.sphere.draw(GL_TRIANGLES)

        if self.texture:
            glDisable(self.texture.target)

        self.fps_display.draw()

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == pyglet.window.key.LEFT:
            self.azimuth -= 5
        elif symbol == pyglet.window.key.RIGHT:
            self.azimuth += 5
        elif symbol == pyglet.window.key.UP:
            self.elevation += 5
        elif symbol == pyglet.window.key.DOWN:
            self.elevation -= 5
        elif symbol == pyglet.window.key.EQUAL:
            self.distance = max(1.0, self.distance - 0.1)
        elif symbol == pyglet.window.key.MINUS:
            self.distance += 0.1

    def update(self, dt: float) -> None:
        self.simulation.step(dt)


def view(simulation: Simulation) -> None:
    window = Show(simulation)
    pyglet.clock.schedule_interval(window.update, 1 / 60.0)
    pyglet.app.run()
