import subprocess

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