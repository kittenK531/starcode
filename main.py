import subprocess
import numpy as np
import matplotlib.pyplot as plt

""" Calculating one orbit """
""" Input:  parameter file 
    Output: follow.out
"""

# CWD = "swifter/swifter_test/"
# wdr = "test"
CWD = "recom/swifter/"
wdr = "example"

particle_id = 6


subprocess.call("rm bin.dat", shell=True, cwd=CWD+wdr)
# subprocess.call("ls", shell=True, cwd=CWD+"test")
subprocess.call("echo 'param.in' | ./../bin/swifter_tu4", shell=True, cwd=CWD+wdr)
subprocess.call("echo 'dump_param1.dat\n6\n20\n' | ./../bin/tool_follow", shell=True, cwd=CWD+wdr)
subprocess.call("ls *.out", shell=True, cwd=CWD+wdr)


""" Plotting the trajectory """
f = open(CWD+wdr+"/follow.out", "r") #TODO: hash file

num_lines = sum(1 for line in open(CWD+wdr+"/follow.out", "r"))

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

    print(listlist)

    # listlist = [float(i) for i in listlist] # list per line in file

    print(listlist)

    x[count], y[count], z[count] = listlist[2], listlist[3], listlist[4]

    count += 1

plt.plot(x, y)
plt.savefig('test.png')

