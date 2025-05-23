"""A simple simulation runner."""
from objects import Planet, Time


class Simulation:
    """Combine a planet with a timekeeper."""

    def __init__(self, planet: Planet, time: Time | None = None) -> None:
        self.planet = planet
        self.time = time or Time()

    def step(self, dt: float) -> None:
        """Advance the simulation by ``dt`` seconds."""
        self.time.advance(dt)
        self.planet.update(dt)
