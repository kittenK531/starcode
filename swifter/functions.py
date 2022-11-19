import subprocess
from pathlib import Path

import numpy as np


def get_hash_name(name):

    hashh = str(np.abs(hash(".")))[:6]

    return name.split(".")[0] + "1" + hashh + "." + name.split(".")[1]


def array2str(array):

    string = " "

    for element in array:

        element = str(element)

        string += element + " "

    return string + "\n"


def amend_infiles(
    name="param.in",
    tp_name="tp.in",
    velocity=np.array([0.0, 1.721420632e-2, 0.0]),
    position=np.array([1.0, 0.0, 0.0]),
    CWD="recom/swifter",
    wdr="example",
):

    cwd = Path(CWD)
    file_dir = cwd.joinpath(Path(wdr))

    infile_hash, tp_hash = get_hash_name(name), get_hash_name(tp_name)

    """ remove hash from last run """  # Trick: appended '1' to each hash of 6 random char
    subprocess.call(
        f"rm {tp_name.split('.')[0]+'1'}* {name.split('.')[0]+'1'}*",
        shell=True,
        cwd=str(file_dir),
    )
    subprocess.call(f"cp {name} {infile_hash}", shell=True, cwd=str(file_dir))
    subprocess.call(
        f"sed -i 's/{tp_name}/{tp_hash}/g' {infile_hash}", shell=True, cwd=str(file_dir)
    )

    """ create new tp file for new vel """
    tp_data = open(file_dir.joinpath(Path(tp_name)), "r+").readlines()[:-2]
    tp_data += [array2str(position)]
    tp_data += [array2str(velocity)]

    tp_create = open(file_dir.joinpath(Path(tp_hash)), "w")
    [tp_create.write(lines) for lines in tp_data]
    tp_create.close()

    return infile_hash, tp_hash


def get_helio_pos_vel(
    CWD="recom/swifter",
    wdr="example",
    outfile_name="follow.out",
    infile_name="param.in",
):  # TODO hash files input + new function to sed input vel and pos

    particle_id, frequency = 6, 1

    cwd = Path(CWD)
    file_dir = cwd.joinpath(Path(wdr))

    outfile_hash = get_hash_name(outfile_name)

    subprocess.call("rm bin.dat *.out", shell=True, cwd=str(file_dir))
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
