from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Planet:
    """Represents a planet moving through space."""

    name: str
    position: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    velocity: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    platforms: List['Platform'] = field(default_factory=list)

    def add_platform(self, platform: 'Platform') -> None:
        """Attach a platform to this planet."""
        self.platforms.append(platform)

    def update(self, dt: float) -> None:
        """Advance the planet and its platforms by ``dt`` seconds."""
        x, y, z = self.position
        vx, vy, vz = self.velocity
        self.position = (x + vx * dt, y + vy * dt, z + vz * dt)
        for platform in self.platforms:
            platform.update(dt)
