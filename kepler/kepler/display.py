import matplotlib.pyplot as plt
from loguru import logger


def start_msg(M, mx, T, h, r, v):

    logger.info(
        "Initialization..."
        + "\n"
        + f"Massive star mass: \t\t{M:.5} Mo\n"
        + f"Dark matter particle mass: \t{mx:.5} GeV\n"
        + f"Total time of simulation is {T:.3} years of interval {h:.5} years\n"
        + f"Initial position: {r} velocity {v}"
    )


def plot(r, alpha, is_3D=False):

    if is_3D:
        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")

        ax.scatter(r[:, 2], r[:, 1], r[:, 0], marker="o")

    else:
        plt.plot(r[:, 0], r[:, 1])

    plt.title(rf"$\alpha = ${alpha:.2}")
    plt.savefig(f"record/alpha={alpha:.2}.png")

    plt.show(block=False)
    plt.close()
