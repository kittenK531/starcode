import subprocess
import numpy as np
import matplotlib.pyplot as plt

""" Calculating one orbit """
""" Input:  parameter file 
    Output: follow.out
"""

CWD = "swifter/swifter_test/"


subprocess.call("rm bin.dat", shell=True, cwd=CWD+"test")
# subprocess.call("ls", shell=True, cwd=CWD+"test")
subprocess.call("./../bin/swifter_tu4", shell=True, cwd=CWD+"test")
subprocess.call("./../bin/tool_follow", shell=True, cwd=CWD+"test")
subprocess.call("ls *.out", shell=True, cwd=CWD+"test")


""" Plotting the trajectory """
f = open(CWD+"test/follow.out", "r") #TODO: hash file

num_lines = sum(1 for line in open(CWD+"test/follow.out", "r"))

x, y, z = np.zeros(num_lines), np.zeros(num_lines), np.zeros(num_lines)

count = 0

for line in f.readlines():

    word_list, listlist = [], []

    lines = line.split(' ')

    for words in lines:

        word_list += [words] if bool(words) else []

    for word in word_list:

        splitn = word.split('\n')

        listlist += [splitn[0]] if len(splitn) > 1 else splitn

    listlist = [float(i) for i in listlist] # list per line in file

    x[count], y[count], z[count] = listlist[2], listlist[3], listlist[4]

    count += 1

plt.plot(x, y)
plt.savefig('test.png')

