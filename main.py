import matplotlib.pyplot as plt
import numpy as np

from swifter.functions import (
    capture,
    get_cs,
    get_init_vel,
    keplerian,
    plot_sun,
    scatter,
)

""" Configure visualization """
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.set_xlabel(r"$x$ / $AU$")
ax.set_ylabel(r"$y$ / $AU$")
ax.set_zlabel(r"$z$ / $AU$")
ax.set_xlim(-0.01, 0.01)
ax.set_ylim(-0.01, 0.01)
ax.set_zlim(-0.01, 0.01)
plt.title(f"Particle trajectory")

""" Plotting sun surface """
r = 0.00465
plot_sun(r, ax)

""" Keplerian oribitals """
m = 1000e3  # DM mass subGeV to super planck (p.7) [in MeV] e3M=G
cs = get_cs(0.5)

initial_position = np.array(
    [0.01, 0.0, 0.0]
)  # circular_vel = 0.172, 0, 0 Scatter: np.array([-0.320, 0.173, 0])
box_muller_velocity = get_init_vel(m)

dt = 0.0001 * 3.6525
N_iter = 3

in_star, pos, vel = keplerian(
    N_iter, dt, initial_position, np.array([-0.320, 0.173, 0]), r, ax
)

in_star, cant_escape = capture(pos, vel)

times = 0

while in_star and (cant_escape == False):

    print(f"{times}th - Scattering")

    pos, vel, Ef = scatter(vel, pos, m, ax, cs)  # simplify

    in_star, cant_escape = capture(pos, vel)

    times += 1

if in_star == False:

    keplerian(1, dt, pos, vel, r, ax)

print(f"Scattered {times} times")

plt.legend()
plt.savefig("testing.png")
