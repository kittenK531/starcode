import matplotlib.pyplot as plt
import numpy as np

from swifter.functions import get_init_vel, keplerian, plot_sun

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.set_xlabel(r"$x$ / $AU$")
ax.set_ylabel(r"$y$ / $AU$")
ax.set_zlabel(r"$z$ / $AU$")
plt.title(f"Particle trajectory")


r = 0.00465
plot_sun(r, ax)


initial_position = np.array([0.01, 0.0, 0.0])  # circular_vel = 0.172, 0, 0
box_muller_velocity = get_init_vel()


dt = 0.0001 * 3.6525
N_iter = 3

keplerian(N_iter, dt, initial_position, box_muller_velocity, r, ax)


plt.legend()


ax.set_xlim(-0.01, 0.01)
ax.set_ylim(-0.01, 0.01)
ax.set_zlim(-0.01, 0.01)


plt.savefig("testing.png")
