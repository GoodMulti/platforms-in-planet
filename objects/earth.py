from dataclasses import dataclass

from .planet import Planet


@dataclass
class Earth(Planet):
    """A simple Earth model referencing a texture image."""

    texture_path: str = "earth.jpg"
