import sys
def main(predicted, actual):
	correct = 0.0
	total = 0.0
	sentCorrect = 0.0
	sentTotal = 0.0
	for p in predicted:
		a = actual.readline()
		pList = p.split(',')
		aList = a.split(',')
		if pList == aList:
			sentCorrect += 1
		sentTotal += 1
		for x in range(0, len(pList)):
			if pList[x] == aList[x]:
				correct +=1
			total += 1
	print str(sentCorrect/sentTotal)
	print str(correct/total)



	

if __name__ == "__main__":
	main(open(sys.argv[1]), open(sys.argv[2]))