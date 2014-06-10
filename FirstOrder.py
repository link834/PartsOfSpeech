import random
 
infilename = "./assignment3/allTraining.txt"
trainingdata = open(infilename).readlines()
 
contextconst = [""]
 
context = contextconst
firstWordProbs = {}
model = {}

total_lines = len(trainingdata)
for line in trainingdata:
	pairs = line.split()
	
	firstWord, firstPos = pairs[0].split('_')
	
	# use for firstWordProbs
	if(firstWord in pZzero):
		firstWordProbs[firstWord] += 1
	else:
		firstWordProbs[firstWord] = 1
	
	for pair in pairs:
		word, pos = pair.split('_')

#	model[str(context)] = model.setdefault(str(context),[])+ [word]
#	context = (context+[word])[1:]
 
#print(model)
 
context = contextconst
for i in range(100):
	word = random.choice(model[str(context)])
	print(word,end=" ")
	context = (context+[word])[1:]
 
print()
