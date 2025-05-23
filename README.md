# platforms-in-planet

A simple project demonstrating a simulator with planets, platforms, and a timekeeper.

## Objects
- `Planet` – represents a moving planet in space.
- `Earth` – simple textured planet subclass.
- `Platform` – a platform that can be attached to a planet.
- `Time` – keeps track of simulation time.

These are defined in the `objects` package.

## Simulation

`Simulation` groups a planet with a `Time` object and advances them together.

## Visualization

The `visualize` package contains a `Show` class which displays a simulation
using pyglet 2.1. If the planet is an `Earth` instance and an image file named
`earth.jpg` is present in the working directory, the texture will be mapped onto
the sphere. Otherwise a solid blue planet is shown. Platforms are rendered as
red spheres. Use the mouse to orbit around the planet and zoom with the scroll
wheel.

