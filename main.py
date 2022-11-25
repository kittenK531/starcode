import matplotlib.pyplot as plt
import numpy as np

from swifter.functions import amend_infiles, formatDTstring, get_helio_pos_vel

fig1, ax = plt.subplots()
"""
ax.set_box_aspect(1)
circ_X, circ_Y, circ__Y = circle(0.00465)
ax.plot(circ_X, circ_Y, color='r', label="sun")
ax.plot(circ_X, circ__Y, color='r')
"""
initial_position, initial_velocity = np.array([0.01, 0.0, 0.0]), np.array(
    [0.0, 0.172, 0.0]  # 0.172
)

initial_r0 = np.sqrt(np.sum(initial_position * initial_position))

plt.title(f"Convergence testing for DT interval")

N, idx = 500, 0
r_record = np.zeros(N)
dt_list = np.linspace(0.00001 * 3.6525, 0.001 * 3.6525, N)

for dt in dt_list:

    param_name, tp_name = amend_infiles(
        velocity=initial_velocity, position=initial_position, dt=formatDTstring(dt)
    )

    x, y, z, vx, vy, vz = get_helio_pos_vel(infile_name=param_name)

    ### ax.plot(x, y, label=f"iteration times: {i}")
    # ax.plot(x, y)

    initial_position = np.array([x[-1], y[-1], z[-1]])
    initial_velocity = np.array([vx[-1], vy[-1], vz[-1]])

    radius = np.sqrt(x * x + y * y + z * z)
    r_diff = radius

    r_record[idx] = r_diff.mean() - initial_r0

    idx += 1


ax.plot(dt_list, r_record)

# get_init_vel()

"""
plt.xlabel(r"$x$ / $AU$")
plt.ylabel(r"$y$ / $AU$")
plt.legend()

ax.set_xlim(-0.006,0.006)
ax.set_ylim(-1e-8,1e-8)
"""


plt.xlabel(r"dt interval / day")
plt.ylabel(r"$\Delta r = r_i - r_0$ / AU")

plt.savefig("convergencetest.png")
### plt.savefig("test.png")
