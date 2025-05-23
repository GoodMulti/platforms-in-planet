from dataclasses import dataclass
from typing import Tuple


@dataclass
class Platform:
    """A movable platform attached to a planet."""

    id: str
    local_position: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    velocity: Tuple[float, float, float] = (0.0, 0.0, 0.0)

    def update(self, dt: float) -> None:
        """Move the platform relative to its current position."""
        x, y, z = self.local_position
        vx, vy, vz = self.velocity
        self.local_position = (x + vx * dt, y + vy * dt, z + vz * dt)
