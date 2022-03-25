import matplotlib.pyplot as plt
from loguru import logger


def start_msg(M, mx, T, h):

    logger.info(
        "Initialization..."
        + "\n"
        + f"Massive star mass: \t\t{M:.5} Mo\n"
        + f"Dark matter particle mass: \t{mx:.5} GeV\n"
        + f"Total time of simulation is {T:.3} of width {h:.5}"
    )


def plot(r, alpha):

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    ax.scatter(r[:, 0], r[:, 1], r[:, 2], marker="o")

    plt.title(rf"$\alpha = ${alpha:.2}")
    plt.savefig(f"record/alpha={alpha}.png")
    plt.show()
    plt.close
