import sys
def main(predicted, actual):
	line = 1
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
		if len(pList) != len(aList):
			print str(line)
		else:
			for x in range(0, len(pList)):
				if pList[x] == aList[x]:
					correct +=1
				total += 1
		line+=1
	print str(sentCorrect/sentTotal)
	print str(correct/total)



	

if __name__ == "__main__":
	main(open(sys.argv[1]), open(sys.argv[2]))