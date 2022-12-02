import matplotlib.pyplot as plt
import numpy as np

from swifter.functions import (
    get_cs,
    get_init_vel,
    keplerian_loop,
    plot_sun,
    scatter_loop,
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
    [0.045, 0, 0]
)  # circular_vel = 0.172, 0, 0 Scatter: np.array([-0.320, 0.173, 0])
box_muller_velocity = get_init_vel(m)
test_vel = 0.2 * np.array([-0.320, 0.173, 0])

dt = 0.0001 * 3.6525
N_iter = 1
in_star, cant_escape = False, False

pos = initial_position
vel = test_vel

total_scatter_times = 0

while (in_star and cant_escape) == False:

    in_star, pos, vel = keplerian_loop(in_star, dt, pos, vel, r, ax)

    pos, vel, in_star, cant_escape, times = scatter_loop(
        in_star, cant_escape, pos, vel, m, ax, cs
    )

    total_scatter_times += times

print(f"Scattered {total_scatter_times} times, captured: {in_star and cant_escape}")
print(box_muller_velocity)

plt.legend()
plt.savefig("testing.png")
