import subprocess
from decimal import Decimal
from pathlib import Path

import numpy as np


def circle(radius):

    x = np.linspace(-1 * radius, radius, 200)
    y = np.sqrt(radius**2 - x**2)

    return x, y, -y


def formatDTstring(dt_float):

    dt_string = "%.4E" % Decimal(str(dt_float))

    return dt_string


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
    position=np.array([0.0, 0.0, 0.0]),
    dt="3.6525E-4",
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
    subprocess.call(
        f"sed -i 's/.*DT.*/DT             {dt}/' {infile_hash}",
        shell=True,
        cwd=str(file_dir),
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
):

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
    f = open(file_dir.joinpath(Path(outfile_hash)), "r")

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

            listlist += [splitn[0]] if (len(splitn) > 1) else splitn

        x[count], y[count], z[count] = listlist[2], listlist[3], listlist[4]
        vx[count], vy[count], vz[count] = listlist[5], listlist[6], listlist[7]

        count += 1

    return x, y, z, vx, vy, vz


def get_init_vel():
    """desired velocity range = 10-1"""

    k = 1  # eV/K
    m = 1000e3  # DM mass subGeV to super planck (p.7) [in MeV] e3M=G
    T = 5e3  # 5.726e0  # K

    norm_const = np.sqrt(T / m)

    vel = np.array(
        [
            np.sqrt(-2 * np.log(np.random.rand()))
            * np.cos(2 * np.pi * np.random.rand())
            for dim in range(3)
        ]
    )

    return norm_const * vel


def enter_star(radius, r0):

    idx = 0
    enter_idx = 0
    append_idx_list = []
    radius_ref = radius

    radius = []

    for ri in radius_ref:

        if ri < r0:

            append_idx_list += [idx]

        idx += 1

    for i in append_idx_list:

        radius += [radius_ref[int(i)]]

    radius = np.array(radius)

    if len(radius) != 0:

        for i in range(len(radius_ref)):

            if radius[0] == radius_ref[i]:

                enter_idx = i

        return True, append_idx_list[0], radius_ref[append_idx_list[0]]

    else:

        return False, 0, 0.0


def first_enter(bool_array, count):

    num_of_true = 0

    bool_array = bool_array[:count]

    for boolean in bool_array:

        if boolean:

            num_of_true += 1

    return False if num_of_true > 0 else True


""" Scattering 

def get_final_vel(ini_vel):

"""
