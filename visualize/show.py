import math
from typing import Optional

import pyglet
from pyglet import gl

from simulation import Simulation
from objects import Earth


class Show(pyglet.window.Window):
    """Display a simulation using pyglet 2.1."""

    def __init__(self, simulation: Simulation, planet_radius: float = 1.0) -> None:
        super().__init__(width=800, height=600, caption="Platform Visualization", resizable=True)
        self.simulation = simulation
        self.radius = planet_radius
        self.azimuth = 45.0
        self.elevation = 20.0
        self.distance = self.radius * 2.5

        pyglet.clock.schedule_interval(self._update, 1 / 60.0)

        self.earth_texture: Optional[pyglet.image.Texture] = None
        if isinstance(self.simulation.planet, Earth):
            try:
                image = pyglet.resource.image(self.simulation.planet.texture_path)
                self.earth_texture = image.get_texture()
            except Exception:
                self.earth_texture = None

        gl.glEnable(gl.GL_DEPTH_TEST)

    # ---------------------------------------------------------
    def _update(self, dt: float) -> None:
        self.simulation.update(dt)

    # ---------------------------------------------------------
    def on_draw(self) -> None:
        self.clear()
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        aspect = self.width / float(self.height)
        gl.gluPerspective(60.0, aspect, 0.1, 100.0)

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()

        x = self.distance * math.cos(math.radians(self.elevation)) * math.sin(math.radians(self.azimuth))
        y = self.distance * math.sin(math.radians(self.elevation))
        z = self.distance * math.cos(math.radians(self.elevation)) * math.cos(math.radians(self.azimuth))
        gl.gluLookAt(x, y, z, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

        self._draw_planet()
        self._draw_platforms()

    # ---------------------------------------------------------
    def _draw_planet(self) -> None:
        if self.earth_texture:
            gl.glEnable(gl.GL_TEXTURE_2D)
            gl.glBindTexture(self.earth_texture.target, self.earth_texture.id)
            quad = gl.gluNewQuadric()
            gl.gluQuadricTexture(quad, True)
            gl.gluQuadricNormals(quad, gl.GLU_SMOOTH)
            gl.gluSphere(quad, self.radius, 36, 18)
            gl.gluDeleteQuadric(quad)
            gl.glDisable(gl.GL_TEXTURE_2D)
        else:
            gl.glColor3f(0.2, 0.2, 1.0)
            quad = gl.gluNewQuadric()
            gl.gluQuadricNormals(quad, gl.GLU_SMOOTH)
            gl.gluSphere(quad, self.radius, 36, 18)
            gl.gluDeleteQuadric(quad)

    # ---------------------------------------------------------
    def _draw_platforms(self) -> None:
        for platform in self.simulation.planet.platforms:
            x, y, z = platform.local_position
            gl.glPushMatrix()
            gl.glTranslatef(x, y, z)
            gl.glColor3f(1.0, 0.0, 0.0)
            quad = gl.gluNewQuadric()
            gl.gluQuadricNormals(quad, gl.GLU_SMOOTH)
            gl.gluSphere(quad, self.radius * 0.05, 16, 8)
            gl.gluDeleteQuadric(quad)
            gl.glPopMatrix()

    # ---------------------------------------------------------
    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int) -> None:
        if buttons & pyglet.window.mouse.LEFT:
            self.azimuth += dx * 0.3
            self.elevation = max(-89.0, min(89.0, self.elevation + dy * 0.3))

    # ---------------------------------------------------------
    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int) -> None:
        self.distance *= math.pow(1.1, -scroll_y)
        self.distance = max(self.radius * 1.2, min(self.radius * 10.0, self.distance))
