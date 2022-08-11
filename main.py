import numpy as np

from kepler import orbit as ko

b = 2

r_0, v_0 = np.array([1, -1 * b, 0]), np.array([0, 3* np.pi, 0])

r = ko.evolve(1.0, r_0, v_0, 1.0, 10.0, 1/365)
