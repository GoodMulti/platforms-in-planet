"""Run a simple simulation visualization."""

from objects import Earth, Platform
from simulation import Simulation
from visualize import view


def main():
    earth = Earth(name="Earth", texture_path="earth.jpg")
    platform = Platform(id="demo")
    earth.add_platform(platform)
    sim = Simulation(earth)
    view(sim)


if __name__ == "__main__":
    main()
