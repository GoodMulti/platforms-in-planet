from dataclasses import dataclass
from typing import Tuple
import math

from .planet import Planet

EARTH_RADIUS_M = 6371000.0


def _latlon_to_unit(lat_deg: float, lon_deg: float) -> Tuple[float, float, float]:
    lat = math.radians(lat_deg)
    lon = math.radians(lon_deg)
    x = math.cos(lat) * math.cos(lon)
    y = math.cos(lat) * math.sin(lon)
    z = math.sin(lat)
    return (x, y, z)


def _vector_angle(a: Tuple[float, float, float], b: Tuple[float, float, float]) -> float:
    dot = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
    dot = max(min(dot, 1.0), -1.0)
    return math.acos(dot)


def _slerp(a: Tuple[float, float, float], b: Tuple[float, float, float], f: float) -> Tuple[float, float, float]:
    angle = _vector_angle(a, b)
    if angle == 0.0:
        return a
    sin_total = math.sin(angle)
    w1 = math.sin((1 - f) * angle) / sin_total
    w2 = math.sin(f * angle) / sin_total
    return (
        w1 * a[0] + w2 * b[0],
        w1 * a[1] + w2 * b[1],
        w1 * a[2] + w2 * b[2],
    )


@dataclass
class Earth(Planet):
    """A simple spherical Earth model."""

    radius: float = EARTH_RADIUS_M

    def latlon_to_xyz(self, lat_deg: float, lon_deg: float, altitude_m: float = 0.0) -> Tuple[float, float, float]:
        unit = _latlon_to_unit(lat_deg, lon_deg)
        r = self.radius + altitude_m
        return (unit[0] * r, unit[1] * r, unit[2] * r)

    # Utility methods reused by Airplane
    @staticmethod
    def unit_from_latlon(lat_deg: float, lon_deg: float) -> Tuple[float, float, float]:
        return _latlon_to_unit(lat_deg, lon_deg)

    @staticmethod
    def slerp_unit(a: Tuple[float, float, float], b: Tuple[float, float, float], f: float) -> Tuple[float, float, float]:
        return _slerp(a, b, f)

    @staticmethod
    def angle_between_units(a: Tuple[float, float, float], b: Tuple[float, float, float]) -> float:
        return _vector_angle(a, b)
