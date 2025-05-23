from dataclasses import dataclass, field
from typing import List, Tuple
import math


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


@dataclass
class Earth(Planet):
    """Earth modeled as a simple sphere."""

    radius: float = 6_371_000.0  # meters

    def surface_coordinates(self, latitude_deg: float, longitude_deg: float) -> Tuple[float, float, float]:
        """Return XYZ coordinates on the Earth's surface for given lat/lon."""
        lat = math.radians(latitude_deg)
        lon = math.radians(longitude_deg)
        x = self.radius * math.cos(lat) * math.cos(lon)
        y = self.radius * math.cos(lat) * math.sin(lon)
        z = self.radius * math.sin(lat)
        return (x, y, z)
