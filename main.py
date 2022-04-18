import numpy as np

from kepler import orbit as ko

r_0, v_0 = np.array([1, 0, 0]), np.array([0, 2 * np.pi, 0])

r = ko.evolve(1.0, r_0, v_0, 1.0, 100.0, 0.00005)
