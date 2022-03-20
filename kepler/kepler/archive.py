def solar2GeV(m):

    m = float(m)

    m_kg = m * 1.989e30
    m_GeV = m_kg / (1.79e-27 * (3e8) ** 2)

    print(f"{m:.3}Mo --> {m_GeV:.3}GeV")

    return m_GeV


def GeV2solar(m):

    m = float(m)

    m_kg = m * (1.79e-27 * (3e8) ** 2)
    m_S = m_kg / 1.989e30

    print(f"{m:.3}GeV --> {m_S:.3}Mo")

    return m_S
