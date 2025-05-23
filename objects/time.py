class Time:
    """Simple timekeeper for the simulation."""

    def __init__(self, start_time: float = 0.0) -> None:
        self.current_time = start_time

    def advance(self, dt: float) -> None:
        """Advance the clock by ``dt`` seconds."""
        self.current_time += dt
