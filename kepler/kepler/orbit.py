import argparse

import numpy as np
from display import plot, start_msg
from functions_wrappers import mass_conversion

""" Passing arguments """
parser = argparse.ArgumentParser()
parser.add_argument("--M", default=1, type=float)
parser.add_argument("--mx", type=float)
parser.add_argument("--T", type=float)
parser.add_argument("--h", type=float)

args = parser.parse_args()

""" Constants initialization """

M, mx = args.M, mass_conversion(args.mx, solar2GeV=False)
G = 4 * np.pi ** 2  # AU^3 Mo^-1 yr^-2

N = int(args.T / args.h)

""" Trajectory tracking """


def g_potential(
    m1, m2, r_rel
):  # TODO: 1) consider volume elements of sun mass accounted version 2) input r array??

    """get gravitational potential value
    Inputs: m1, m2, r_rel (scalar)
    Outputs: scalar value
    """

    return -1 * G * m1 * m2 / r_rel


def g_acc_theo(m1, r_1, r_2):

    """get gravitational potential value
    Inputs: m1, m2      (scalar)
            r_1, r_2    (array)
    Outputs: acceleration array (1,3)
    """

    r_rel = r_1 - r_2
    rrel = np.linalg.norm(r_rel)

    return -1 * G * m1 / rrel ** 3 / 2 * r_rel
    # return -3 * G * m1 / (rrel * rrel) * r_rel #, r_rel


def evolve(r_0, v_0, alpha, N=N):

    """get array of x evolution aroound the rest frame of star
    Inputs: r_0, v_0    (array)
    Output: r (array)
    """

    # Initialization #
    r_star = np.zeros(3)
    r, v, a = np.zeros((N, 3)), np.zeros((N, 3)), np.zeros((N, 3))

    r[0], v[0] = r_0, alpha * v_0
    a[0] = g_acc_theo(M, r[0], r_star)

    for i in range(N - 1):

        r[i + 1] = r[i] + v[i] * args.h + 0.5 * a[i] * (args.h * args.h) / 2
        v[i + 1] = v[i] + a[i] * args.h / 2
        a[i + 1] = g_acc_theo(M, r[i + 1], r_star)
        v[i + 1] = v[i + 1] + a[i + 1] * args.h / 2

    return r


""" Execute """
for alpha in [0.8, 0.9, 1.0, 1.05]:
    start_msg(M, args.mx, args.T, args.h)
    r = evolve(np.array([1, 0, 0]), np.array([0, 2 * np.pi, 0]), alpha)
    plot(r, alpha)
