from dataclasses import dataclass
from typing import Tuple
from .planet import Planet


@dataclass
class Earth(Planet):
    """A planet with optional surface texture."""

    texture_path: str | None = None

    def latlon_to_xyz(self, lat: float, lon: float, radius: float = 1.0) -> Tuple[float, float, float]:
        """Convert latitude/longitude in degrees to 3D coordinates."""
        import math

        lat_r = math.radians(lat)
        lon_r = math.radians(lon)
        x = radius * math.cos(lat_r) * math.cos(lon_r)
        y = radius * math.sin(lat_r)
        z = radius * math.cos(lat_r) * math.sin(lon_r)
        return x, y, z
