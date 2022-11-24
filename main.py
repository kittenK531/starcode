import matplotlib.pyplot as plt
import numpy as np

from swifter.functions import amend_infiles, get_helio_pos_vel, get_init_vel

param_name, tp_name = amend_infiles(
    velocity=np.array([0.0, 1.921420632e-2, 0.0]), position=np.array([1.0, 0.0, 0.0])
)

x, y, z, vx, vy, vz = get_helio_pos_vel(infile_name=param_name)

get_init_vel()


fig1, ax = plt.subplots()
ax.set_box_aspect(1)
ax.plot([0], [0], "ro")
ax.plot(x, y)
# ax.set_xlim(np.min(x),np.max(x))
ax.set_title("new")
plt.savefig("test.png")
