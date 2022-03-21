def mass_conversion(m, solar2GeV=True):
    """Convert input mass unit
    m: input mass

    solar2GeV:  (True)  Mo  --> GeV
                (False) GeV --> Mo
    """

    Mo_, GeV_ = 1.989e30, 1.79e-27 * (3e8) ** 2

    return (float(m) * Mo_) / (GeV_) if solar2GeV else (float(m) * GeV_) / Mo_
