import shutil
from datetime import datetime
from pathlib import Path

import imageio
import matplotlib.pyplot as plt
from loguru import logger

target = Path.joinpath(Path.cwd(), Path("kepler/kepler/record"))


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

    fig = plt.figure()

    if is_3D:
        ax = fig.add_subplot(projection="3d")

        ax.scatter(r[:, 2], r[:, 1], r[:, 0], marker="o")
        ax.set_aspect("auto")
        ax.set_zlim(-2, 2)
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)

    else:
        ax = fig.add_subplot(111)
        ax.plot(r[:, 0], r[:, 1])
        ax.set_aspect("equal")
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)

    plt.title(rf"$\alpha = ${alpha:.2}")
    plt.savefig(str(Path.joinpath(target, Path(f"alpha={alpha:.2}.png"))))
    plt.show(block=False)
    plt.close()


def combine(foldername="kepler/kepler/record", name_1="flipped", name_2="crystal"):

    from PIL import Image

    im1 = Image.open(f"{foldername}/{name_1}.png")
    im2 = Image.open(f"{foldername}/{name_2}.png")

    dst = Image.new("RGB", (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))

    dst.save(f"convergence.png")


def make_GIF(foldername="kepler/kepler/record", clean=False):

    current_time = datetime.now()

    filename = [child for child in target.iterdir()]

    name_out = (
        f"{foldername}/{current_time.day}{current_time.hour}{current_time.minute}.gif"
    )

    with imageio.get_writer(
        name_out,
        mode="I",
    ) as writer:

        for name in filename:

            image = imageio.imread(name)
            writer.append_data(image)

    print(f"animation saved as {name_out}")

    if clean:

        shutil.rmtree(f"{foldername}")
