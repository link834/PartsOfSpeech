
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
	fileName = './assignment3/devtest.txt'
	training_data = open(fileName, 'r').readlines()
	output = open('./devtest.actual', 'w+')

	# total_lines = len(training_data)
	output.write("\n\n\n")
	count = 1
	for t_line in training_data:
		for tupple in t_line.split():
			tupple = tupple.split("_")
			output.write(tupple[0] + " " + tupple[1] + "\n")
			# output.write(tupple[0] + "\n")
		output.write("\n\n\n")

    
if __name__ == '__main__':
	main()
