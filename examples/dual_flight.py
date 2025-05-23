import time as realtime

from objects import Earth, Airplane, Time
from simulation import Simulation


LAX = (33.9416, -118.4085)
PHL = (39.8744, -75.2424)
ATL = (33.6407, -84.4277)

SIM_DURATION = 6 * 3600  # six hours
REAL_DURATION = 60  # one minute
STEPS = 120  # number of real-time steps


def main() -> None:
    earth = Earth(name="Earth")
    clock = Time()

    plane1 = Airplane(
        id="LAX->PHL",
        earth=earth,
        start_lat=LAX[0],
        start_lon=LAX[1],
        end_lat=PHL[0],
        end_lon=PHL[1],
        duration=SIM_DURATION,
        altitude=11000.0,
    )

    plane2 = Airplane(
        id="ATL->LAX",
        earth=earth,
        start_lat=ATL[0],
        start_lon=ATL[1],
        end_lat=LAX[0],
        end_lon=LAX[1],
        duration=SIM_DURATION,
        altitude=11000.0,
    )

    sim = Simulation(planet=earth, time=clock)
    sim.add_platform(plane1)
    sim.add_platform(plane2)

    sim_dt = SIM_DURATION / STEPS
    real_dt = REAL_DURATION / STEPS

    for step in range(STEPS + 1):
        sim.step(sim_dt)
        if step % 10 == 0:
            hours = clock.current_time / 3600
            pos1 = plane1.local_position
            pos2 = plane2.local_position
            print(f"t={hours:.1f}h")
            print(f"  {plane1.id} at {pos1}")
            print(f"  {plane2.id} at {pos2}")
        realtime.sleep(real_dt)


if __name__ == "__main__":
    main()
