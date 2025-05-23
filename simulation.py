from dataclasses import dataclass, field
from typing import List

from objects.planet import Planet
from objects.platform import Platform
from objects.time import Time


@dataclass
class Simulation:
    """Advance a planet and its platforms with a timekeeper."""

    planet: Planet
    time: Time
    platforms: List[Platform] = field(default_factory=list)

    def add_platform(self, platform: Platform) -> None:
        self.platforms.append(platform)
        self.planet.add_platform(platform)

    def step(self, dt: float) -> None:
        """Advance the simulation by ``dt`` seconds."""
        self.planet.update(dt)
        self.time.advance(dt)
