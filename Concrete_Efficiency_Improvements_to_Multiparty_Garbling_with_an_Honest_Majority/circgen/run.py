

import sys
import os
import subprocess

RANDOM = "43739841701238781571456410093f43"
VERSION = 14

numbits = {}
numbits[3]=10
numbits[5]=11
numbits[7]=13
numbits[9]=13
numbits[11]=14
numbits[13]=14
numbits[15]=15
numbits[17]=15
numbits[19]=16
numbits[21]=16
numbits[23]=16
numbits[25]=16


if __name__ == '__main__':
	nargs = len(sys.argv)
	if nargs == 2:
		nparties = int(sys.argv[1])
		circuitfile = "circgen/%.2dadder%dbits.circ"%(nparties,numbits[nparties])
		inputfile = 'circgen/input16bits.inp'
		ipfile = 'parties'
		local = 'yes'
	elif not nargs == 6:
		# print "run.py <nparties> <circuitfile> <inputfile> <ipfile> <local('yes'/'no')>"
		print "using default: nparties=3, circtuitfile='circgen/03adder10bits.circ', inputfile='circgen/input16bits.inp', ipfile='parties', local='yes'"
		nparties = 3
		circuitfile = 'circgen/03adder10bits.circ'
		inputfile = 'circgen/input16bits.inp'
		ipfile = 'parties'
		local = 'yes'
	else:
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



