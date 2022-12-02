import matplotlib.pyplot as plt
import numpy as np

from swifter.functions import (
    amend_infiles,
    enter_star,
    first_enter,
    formatDTstring,
    get_helio_pos_vel,
    get_init_vel,
)

fig = plt.figure()
ax = plt.axes(projection="3d")


r = 0.00465
u, v = np.linspace(0, 2 * np.pi, 100), np.linspace(0, np.pi, 100)
x = r * np.outer(np.cos(u), np.sin(v))
y = r * np.outer(np.sin(u), np.sin(v))
z = r * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, cmap=plt.cm.YlGnBu_r, antialiased=False, alpha=0.2)

box_muller_velocity = get_init_vel()

"""
initial_position, initial_velocity = np.array([0.01, 0.0, 0.0]), np.array(
    [0.172, 0.0, 0.0]  # 0.172
)
"""
initial_position, initial_velocity = np.array([0.01, 0.0, 0.0]), np.array(
    box_muller_velocity  # 0.172
)

initial_r0 = np.sqrt(np.sum(initial_position * initial_position))

plt.title(f"Particle trajectory")

N, idx = 500, 0
r_record = np.zeros(N)
dt = 0.0001 * 3.6525
entered_star = False
N_iter = 3
flag_arr = np.zeros(N_iter)  # Zero = False

num_enter = 0

for i in range(N_iter):

    param_name, tp_name = amend_infiles(
        velocity=initial_velocity, position=initial_position, dt=formatDTstring(dt)
    )

    x, y, z, vx, vy, vz = get_helio_pos_vel(infile_name=param_name)

    # ax.plot3D(x, y, z)

    initial_position = np.array([x[-1], y[-1], z[-1]])
    initial_velocity = np.array([vx[-1], vy[-1], vz[-1]])

    radius = np.sqrt(x * x + y * y + z * z)

    enter_flag, enter_idx, r_enter = enter_star(radius, r0=r)

    flag_arr[i] = enter_flag

    entered_star = entered_star or enter_flag

    if entered_star and first_enter(flag_arr, i):

        enter_coord = np.array([x[enter_idx], y[enter_idx], z[enter_idx]])
        enter_vel = np.array([vx[enter_idx], vy[enter_idx], vz[enter_idx]])

        ax.scatter3D(x[enter_idx], y[enter_idx], z[enter_idx], cmap="Greens")
        ax.plot3D(x[:enter_idx], y[:enter_idx], z[:enter_idx])

    if not enter_flag:

        ax.plot3D(x, y, z)

    idx += 1

try:
    print(f"enter coord:{enter_coord}, enter vel: {enter_vel}")

except:
    print("No enter")


print(box_muller_velocity)


ax.set_xlabel(r"$x$ / $AU$")
ax.set_ylabel(r"$y$ / $AU$")
ax.set_zlabel(r"$z$ / $AU$")
plt.legend()


ax.set_xlim(-0.01, 0.01)
ax.set_ylim(-0.01, 0.01)
ax.set_zlim(-0.01, 0.01)


plt.savefig("testing.png")
