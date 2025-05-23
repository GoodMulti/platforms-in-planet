# platforms-in-planet

A simple project demonstrating a simulator with planets, platforms, and a timekeeper.

## Objects
- `Planet` – represents a moving planet in space.
- `Platform` – a platform that can be attached to a planet.
- `Time` – keeps track of simulation time.
- `Earth` – spherical Earth with helpers to convert latitude/longitude.
- `Airplane` – platform that flies along a great-circle route.

These are defined in the `objects` package.

## Example

The `examples` folder contains `dual_flight.py`, illustrating two airplanes
flying simultaneously from Los Angeles to Philadelphia and from Atlanta to
Los Angeles. The script compresses six hours of simulated flight into one real
minute.

Run it with:

```bash
python -m examples.dual_flight
```
