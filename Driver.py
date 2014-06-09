
import sys
import math
import time

#need to know
# P( Z0 )
# P( Xk | Zk )
# P( Xk+1 | Zk ))

def main():
	
	pZzero = {}

	print "opening training file"
	fileName = './assignment3/allTraining.txt'
	training_data = open(fileName, 'r').readlines()

	total_lines = len(training_data)
	#print total_lines

	for t_line in training_data:
		t_pairs = t_line.split()
		# used to find P( Z0 )
		first_w, first_pos = t_pairs[0].split('_')

		if(first_pos in pZzero):
			pZzero[first_pos] += 1
		else:
			pZzero[first_pos] = 1

		print "%s %d %f" % (first_pos, pZzero[first_pos], float(pZzero[first_pos]) / float(total_lines))
		for t_pair in t_pairs:
			word, pos = t_pair.split('_')

    
if __name__ == '__main__':
	main()
