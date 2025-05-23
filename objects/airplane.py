from typing import Tuple

from .platform import Platform
from .earth import Earth


class Airplane(Platform):
    """A simple airplane moving along a great-circle path."""

    def __init__(
        self,
        id: str,
        earth: Earth,
        start_lat: float,
        start_lon: float,
        end_lat: float,
        end_lon: float,
        altitude: float = 10000.0,
        duration: float = 21600.0,
    ) -> None:
        super().__init__(id)
        self.earth = earth
        self.start_lat = start_lat
        self.start_lon = start_lon
        self.end_lat = end_lat
        self.end_lon = end_lon
        self.altitude = altitude
        self.duration = duration
        self._elapsed = 0.0

        self._start_unit = Earth.unit_from_latlon(start_lat, start_lon)
        self._end_unit = Earth.unit_from_latlon(end_lat, end_lon)
        angle = Earth.angle_between_units(self._start_unit, self._end_unit)
        self.distance = earth.radius * angle
        self.speed = self.distance / self.duration
        self.local_position = earth.latlon_to_xyz(start_lat, start_lon, altitude)

    def update(self, dt: float) -> None:
        self._elapsed += dt
        f = min(self._elapsed / self.duration, 1.0)
        unit = Earth.slerp_unit(self._start_unit, self._end_unit, f)
        r = self.earth.radius + self.altitude
        self.local_position = (unit[0] * r, unit[1] * r, unit[2] * r)
