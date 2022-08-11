import numpy as np
from kepler.functions_wrappers import mass_conversion
import matplotlib.pyplot as plt
from tqdm import tqdm

G, m_x, M = 4 * np.pi ** 2, 3e-6 , 1 # mass_conversion(100, solar2GeV=False)

k = G * m_x * M

mu = m_x * M / (m_x + M)

R = 0.00465047 # AU

def U_eff(r, b, v0):

    l = m_x * np.linalg.norm(v0) * b

    return -1 * k / r + l *l / (2 * mu * r*r), l

def Energy(m, v):

    return 0.5 * m * v*v

def manuver(x_p, x_s, v_p, h, l): # p: particle, s: star

    r = np.linalg.norm(x_p - x_s)

    mag =  - 1 * k / r**3 * (1/m_x)
    mag_2 = l*l / (mu * r**4) * (1/m_x)

    acc = (mag) * x_p

    v_p = v_p + acc * h
    x_p = x_p + v_p * h + 0.5 * acc * h*h

    return x_p, v_p, (mag)* x_p

b = 0

x_p = np.array([1, b])
x_s = np.zeros(len(x_p))

v_0 = np.array([0, 2 * np.pi])

l = U_eff(np.linalg.norm(x_p - x_s), b, v_0)[1]

for idx in tqdm(range(200)):

    x_p, v_p, acc = manuver(x_p, x_s, v_0, 0.05, l)

    plt.scatter(x_p[0], x_p[1], color="blue", marker = ".")

plt.scatter(0.5, x_s[0], color="red", marker = "o")

plt.xlim(-0.5,1.5)
plt.ylim(-0.5,0.5)
plt.savefig("gg.png")
plt.show(block=False)
    












