import matplotlib.pyplot as plt
import numpy as np

from swifter.functions import get_final_vel, get_init_vel, keplerian, plot_sun

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

initial_position = np.array([0.01, 0.0, 0.0])  # circular_vel = 0.172, 0, 0
box_muller_velocity = get_init_vel(m)

dt = 0.0001 * 3.6525
N_iter = 3

in_star, enter_pos, enter_vel = keplerian(
    N_iter, dt, initial_position, box_muller_velocity, r, ax
)

get_final_vel(box_muller_velocity, m)

plt.legend()
plt.savefig("testing.png")
