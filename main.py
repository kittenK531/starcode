import subprocess
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def get_hash_code():

    return str(np.abs(hash(".")))[:6]


def get_helio_pos_vel(
    CWD="recom/swifter",
    wdr="example",
    outfile_name="follow.out",
    infile_name="param.in",
):  # , outfile_name, infile_name) #TODO hash files input + new function to sed input vel and pos

    particle_id, frequency = 6, 1

    cwd = Path(CWD)
    file_dir = cwd.joinpath(Path(wdr))

    outfile_hash = (
        outfile_name.split(".")[0] + get_hash_code() + "." + outfile_name.split(".")[1]
    )

    subprocess.call("rm bin.dat *.out", shell=True, cwd=str(file_dir))
    subprocess.call("ls -l *.out", shell=True, cwd=str(file_dir))
    subprocess.call(
        f"echo '{infile_name}' | ./../bin/swifter_tu4", shell=True, cwd=str(file_dir)
    )
    subprocess.call(
        f"echo 'dump_param1.dat\n{particle_id}\n{frequency}\n' | ./../bin/tool_follow",
        shell=True,
        cwd=str(file_dir),
    )
    subprocess.call(f"cp {outfile_name} {outfile_hash}", shell=True, cwd=str(file_dir))

    """ Getting the pos, vel via scanf """
    f = open(file_dir.joinpath(Path(outfile_hash)), "r")  # TODO: hash file

    num_lines = sum(1 for line in open(file_dir.joinpath(Path(outfile_hash)), "r"))

    x, y, z = np.zeros(num_lines), np.zeros(num_lines), np.zeros(num_lines)
    vx, vy, vz = np.zeros(num_lines), np.zeros(num_lines), np.zeros(num_lines)

    count = 0

    for line in f.readlines():

        word_list, listlist = [], []

        lines = line.split(" ")

        for words in lines:

            word_list += [words] if bool(words) else []

        for word in word_list:

            splitn = word.split("\n")

            splitn = (
                ["-1.0"] if ("*******" in splitn) else splitn
            )  # fixing the display bug

            listlist += [splitn[0]] if (len(splitn) > 1) else splitn

        try:
            x[count], y[count], z[count] = listlist[2], listlist[3], listlist[4]
            vx[count], vy[count], vz[count] = listlist[5], listlist[6], listlist[7]
        except:
            print(f"disregarded count {count}")

        count += 1

    return x, y, z, vx, vy, vz


x, y, z, vx, vy, vz = get_helio_pos_vel()

fig1, ax = plt.subplots()
ax.set_box_aspect(1)
ax.plot(x, y)
plt.savefig("test.png")
