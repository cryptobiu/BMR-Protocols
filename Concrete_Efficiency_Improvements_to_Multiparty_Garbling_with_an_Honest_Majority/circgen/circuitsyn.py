


# let numbits be S, then this generates an ADD circuits which receives S bits from each party x1,...xn and outputs (SUM{x_i} mod S).
# this is done by (SUM{x_i} mod S) = ( ... ( (x1+x2 mod S) + x3 mod S) + ... + xn mod S)
# so the circuit is of depth nS and operates in n phases: in the i-th phase (for i>=2) it adds (SUM xj mod S) + xi mod S (where j=1,...,i-1)
# given two numbers x=(xS,...,x3,x2,x1) and y=(yS,...,y3,y2,y1) then the circuit computes z=(zS,...,z3,z2,z1)=x+y mod S by 
# 1) Initialize ci=0 for i=1,...,S-1
# 2) Set z1 = x1 XOR y1
#		 c1 = x1 AND y1
# 3) For i=2...S do:
#		zi = ci XOR xi XOR yi
#		ci+1 = (ci AND xi) OR (ci AND yi) OR (xi AND yi)
# 4) Finally set zS = cS XOR xS XOR yS.

# Note that we don't care about the last carry bit cS+1 because it gets reduced anyway by the mod S operation.
# In total we have 1 + 5(S-1) gates (AND or OR) per addition (the XOR gates are free)
# Total number of wires:
#		nS for inputs
#		2S-1 for every addition (every addition adds the variables z and c for every position)

import math
from mpmath import *

NL = "\n" #new line
XOR = "0110"
AND = "0001"
OR  = "0111"#currently not supported by the protocol
NOT = "10"#seems to be a bug when using OR
ONE = 0 #assume that the first bit of P0 is 1

def gen_adder_2(left_w, right_w, next_w):
	gates = ""
	S = len(left_w)
	if not S == len(right_w):
		print "Error |left_w| != |right_w|"
		exit(1)

	carry_w = -1
	result_w = []
	for i in reversed(range(S)):
		if i == (S-1): #the LSB
			gates += "%d %d %d %s"%(left_w[i],right_w[i],next_w, XOR) + NL
			gates += "%d %d %d %s"%(left_w[i],right_w[i],next_w+1, AND) + NL

			result_w.append(next_w)
			carry_w = next_w + 1
			next_w = next_w + 2
		elif i > 0:
			gates += "%d %d %d %s"%(left_w[i],right_w[i],next_w, XOR) + NL
			gates += "%d %d %d %s"%(next_w,carry_w,next_w+1, XOR) + NL
			result_w.append(next_w+1)
			next_w = next_w + 2

			gates += "%d %d %d %s"%(carry_w,left_w[i],next_w, AND) + NL
			gates += "%d %d %d %s"%(carry_w,right_w[i],next_w+1, AND) + NL
			gates += "%d %d %d %s"%(left_w[i],right_w[i],next_w+2, AND) + NL

			# OR gates not supported, instead using OR(a,b) = NOT(NOT(a) AND NOT(b)) where NOT(a) is XOR(a,ONE)
			# gates += "%d %d %d %s"%(next_w,next_w+1,next_w+3, OR) + NL
			# gates += "%d %d %d %s"%(next_w+2,next_w+3,next_w+4, OR) + NL
			gates += "%d %d %d %s"%(next_w, ONE, next_w+3, XOR) + NL
			gates += "%d %d %d %s"%(next_w+1, ONE, next_w+4, XOR) + NL
			gates += "%d %d %d %s"%(next_w+3,next_w+4,next_w+5, AND) + NL
			gates += "%d %d %d %s"%(next_w+5, ONE, next_w+6, XOR) + NL

			gates += "%d %d %d %s"%(next_w+2, ONE, next_w+7, XOR) + NL
			gates += "%d %d %d %s"%(next_w+6, ONE, next_w+8, XOR) + NL
			gates += "%d %d %d %s"%(next_w+7,next_w+8,next_w+9, AND) + NL
			gates += "%d %d %d %s"%(next_w+9, ONE, next_w+10, XOR) + NL

			carry_w = next_w+10
			next_w = next_w+11
		else:#i==0, the MSB
			gates += "%d %d %d %s"%(left_w[i],right_w[i],next_w, XOR) + NL
			gates += "%d %d %d %s"%(next_w,carry_w,next_w+1, XOR) + NL
			result_w.append(next_w+1)
			next_w = next_w + 2

	return (gates, next_w, list(reversed(result_w)))



def gen_adder(n,S):

	#inputs
	inputs = ""
	input_w = {}
	for i in range(1,n+1):
		pid = i-1
		if pid == 0:
			num_in_wires = S+1 #becuae P0 enters the global 1 as its first input
			input_w[i] = list(range(1,S+1))
		else:
			num_in_wires = S
			input_w[i] = list(range(1+(i-1)*S,1+i*S))
		inputs += "P%d %d"%(pid,num_in_wires) + NL
		if pid == 0:
			inputs += "0" + NL
		for j in input_w[i]:
			inputs += "%d"%j + NL

	#gates
	gates = ""
	next_w = 1+n*S
	result_w = input_w[1]
	for i in range(2,n+1):
		(g,next_w,result_w) = gen_adder_2(result_w, input_w[i],next_w)
		gates += g
	
	#align outputs to be ordered until the end
	out_w = []
	gates += "%d %d %d %s"%(0,0,next_w, XOR) + NL #just having a wire with constant value 0
	ZERO = next_w
	next_w += 1
	for i in range(len(result_w)):
		gates += "%d %d %d %s"%(ZERO,result_w[i],next_w+i, XOR) + NL
		out_w.append(next_w+i)

	#outpus
	outputs = "Out %d"%(S) + NL
	for w in out_w:
		outputs += "%d"%(w) + NL


	circ = "# a row that has to be here..." + NL
	ngates = gates.count(NL)
	nwires = n*S+1 + ngates
	circ += "%d %d %d"%(ngates,n,nwires) + NL
	circ += inputs
	circ += outputs
	circ += "#" + NL
	circ += gates
	
	return circ


if __name__ == '__main__':
	q = 100

	add_circ = gen_adder(24,16)
	print add_circ

	# for n in range(3,25):
	# 	q_infty = binomial(n,2)*q+1
	# 	S1 = q_infty*2+1
	# 	log = math.log(S1,2)
	# 	S2 = 2**ceil(log)
	# 	add_circ = gen_adder(n,ceil(log))