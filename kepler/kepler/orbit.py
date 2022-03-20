""" Numerical values """
Mo_ = 1.989e30
GeV_ = 1.79e-27 * (3e8) ** 2

""" Constants initialization """

Mo = 1  # Mo
Mx = 0.05  # Mo
G = 3  # Mo... #TODO: fix the unit and number (finalize the units)


""" Unit Conversion """


def mass_conversion(m, solar2GeV=True):

    m = float(m)

    return (m * Mo_) / (GeV_) if solar2GeV else (m * GeV_) / Mo_


""" Exact trajectory tracking """


def g_potential(
    m1, m2, r_rel
):  # TODO: 1) consider volume elements of sun mass accounted version 2) input r array??

    """get gravitational potential value
    Inputs: m1, m2, r_rel (scalar)
    Outputs: scalar value
    """

    return -1 * G * m1 * m2 / r_rel


""" Execute """

print(mass_conversion(0.1, False))
