

import sys
import os
import subprocess

RANDOM = "43739841701238781571456410093f43"
VERSION = 14

if __name__ == '__main__':
	nargs = len(sys.argv)
	if not nargs == 6:
		print "run.py <nparties> <circuitfile> <inputfile> <ipfile> <local('yes'/'no')>"
	nparties = int(sys.argv[1])
	circuitfile = sys.argv[2]
	inputfile = sys.argv[3]
	ipfile = sys.argv[4]
	local = sys.argv[5]

	for i in range(nparties):
		if local == "yes":
			partyid = i
		else:
			partyid = -1
		CMD = '''xterm -hold -e "./BMRPassive.out %d %s %s %s %s %d"'''%(partyid,circuitfile,inputfile, ipfile, RANDOM,VERSION)
		print CMD
		subprocess.Popen(CMD, shell=True)
		# os.system(CMD)



