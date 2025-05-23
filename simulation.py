from dataclasses import dataclass, field

from objects import Planet, Time


@dataclass
class Simulation:
    """Simple container for a planet and simulation time."""

    planet: Planet
    time: Time = field(default_factory=Time)

    def update(self, dt: float) -> None:
        """Advance the simulation by ``dt`` seconds."""
        self.time.advance(dt)
        self.planet.update(dt)
