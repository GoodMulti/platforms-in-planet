# platforms-in-planet

A simple project demonstrating a simulator with planets, platforms, and a timekeeper.

## Objects
- `Planet` – represents a moving planet in space.
- `Platform` – a platform that can be attached to a planet.
- `Time` – keeps track of simulation time.
- `Earth` – a `Planet` subclass with optional texture mapping.

These are defined in the `objects` package.

## Visualization

The optional `visualize` package uses **pyglet 2.1** to display a planet and any
attached platforms.  If an `earth.jpg` file is found in the working directory it
will be mapped onto the planet surface as a texture; otherwise the planet is
rendered in blue.

To run the example viewer:

```bash
python -m example.run_example
```
