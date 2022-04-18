import numpy as np
from tqdm import tqdm

from kepler.archive import print_dist
from kepler.display import plot, start_msg
from kepler.functions_wrappers import mass_conversion

""" Constants initialization """

M, mx = 1.0, mass_conversion(0.001, solar2GeV=False)
G = 4 * np.pi ** 2  # AU^3 Mo^-1 yr^-2

T, h = 1.1, 0.00005  # yr

N = int(T / h)

""" Trajectory tracking """


def g_acc_theo(m1, r_1, r_2):

    """get gravitational potential value
    Inputs: m1, m2      (scalar)
            r_1, r_2    (array)
    Outputs: acceleration array (1,3)
    """

    r_rel = r_1 - r_2
    rrel = np.linalg.norm(r_rel)

    return (-1 * G * m1 / (rrel ** (3 / 2))) * r_rel


def evolve(M, r_0, v_0, alpha, T, h, check_radius=False):

    start_msg(M, mx, T, h, r_0, v_0)

    """get array of x evolution aroound the rest frame of star
    Inputs: r_0, v_0    (array)
    Output: r (array)
    """

    N = int(T / h)

    # Initialization #
    r_star = np.zeros(3)
    r, v, a = np.zeros((N, 3)), np.zeros((N, 3)), np.zeros((N, 3))

    r[0], v[0], a[0] = r_0, alpha * v_0, g_acc_theo(M, r_0, r_star)

    for i in tqdm(range(N - 1)):

        r[i + 1] = r[i] + v[i] * h + 0.5 * a[i] * (h * h) / 2
        v[i + 1] = v[i] + a[i] * h / 2
        a[i + 1] = g_acc_theo(M, r[i + 1], r_star)
        v[i + 1] = v[i + 1] + a[i + 1] * h / 2

        if check_radius:
            print_dist(r[i + 1])

    plot(r, alpha, is_3D=False)

    return r


# bounds of the alpha
# 100-300 km/s
""" Execute """

"""
r_0, v_0 = np.array([1, 0, 0]), np.array([0, 2 * np.pi, 0])
for i in range(63):
    alpha = 0.1 + i * 0.02
    r = evolve(M, r_0, v_0, alpha, T, h)

make_GIF()
"""
