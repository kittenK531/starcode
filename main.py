import matplotlib.pyplot as plt
import numpy as np

from swifter.functions import amend_infiles, get_helio_pos_vel

fig1, ax = plt.subplots()
ax.set_box_aspect(1)

initial_position, initial_velocity = np.array([1.0, 0.0, 0.0]), np.array(
    [0.0, 3.121420632e-2, 0.0]
)

plt.title(f"Particle trajectory")

for i in range(3):

    param_name, tp_name = amend_infiles(
        velocity=initial_velocity, position=initial_position
    )

    x, y, z, vx, vy, vz = get_helio_pos_vel(infile_name=param_name)

    ax.plot(x, y, label=f"iteration times: {i}")

    initial_position = np.array([x[-1], y[-1], z[-1]])
    initial_velocity = np.array([vx[-1], vy[-1], vz[-1]])

get_init_vel()

ax.plot([0], [0], "ro")

plt.xlabel(r"$x$ / $AU$")
plt.ylabel(r"$y$ / $AU$")
plt.legend()

# ax.set_xlim(-1*np.max(x)-0.1,np.max(x)+0.1)
# ax.set_ylim(-10,10)

plt.savefig("test.png")
