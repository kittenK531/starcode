import argparse

import numpy as np
from display import start_msg
from functions_wrappers import mass_conversion

""" Passing arguments """
parser = argparse.ArgumentParser()
parser.add_argument("--M", default=1, type=float)
parser.add_argument("--mx", type=float)

args = parser.parse_args()


""" Constants initialization """

M, mx = args.M, mass_conversion(args.mx, solar2GeV=False)
G = 4 * np.pi  # AU^3 Mo^-1 yr^-2

""" Trajectory tracking """


def g_potential(
    m1, m2, r_rel
):  # TODO: 1) consider volume elements of sun mass accounted version 2) input r array??

    """get gravitational potential value
    Inputs: m1, m2, r_rel (scalar)
    Outputs: scalar value
    """

    return -1 * G * m1 * m2 / r_rel


""" Execute """
start_msg(M, args.mx)
