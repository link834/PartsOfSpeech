import random

# picks words from a given dictionary
def pickWord(dictionary):
	rand_num = random.uniform(0.0, 1.0)
	prev_prob = 0.0
	first_word = ""
	for pkey in dictionary:
		first_word = pkey
		if((prev_prob + dictionary[pkey]) < rand_num):
			prev_prob += dictionary[pkey]
		else:
			break

	return first_word

#########################
#  PROGRAM BEGINS HERE  #
#########################
infilename = "./assignment3/allTraining.txt"
trainingdata = open(infilename).readlines()
 
contextconst = ""
 
context = contextconst
firstWordProbs = {}
model = {}

total_lines = len(trainingdata)
prob_constant = float(1.0 / float(total_lines))
#prob_constant = 1

for line in trainingdata:
	pairs = line.split()
	
	firstWord, firstPos = pairs[0].split('_')
	
	# build up firstWordProbs
	if(firstWord in firstWordProbs):
		firstWordProbs[firstWord] += prob_constant
	else:
		firstWordProbs[firstWord] = prob_constant
	
	# use for context probs
	for pair in pairs:
		word, pos = pair.split('_')
		if(str(context) in model):
			if(word in model[str(context)]):
				model[str(context)][word] += 1
			else:
				model[str(context)][word] = 1
		else:
			model[str(context)] = {word: 1}

		context = word

# calculate context probablities
for mkey in model:
	#print(mkey,end=": ")
	numWords = 0
	for wkey in model[mkey]:
		numWords += model[mkey][wkey]
	for wkey in model[mkey]:
		#print(wkey,end="=")
		model[mkey][wkey] = float(float(model[mkey][wkey]) / float(numWords))
		#print(model[mkey][wkey], end=" ")
	#print()

		
# begin printing words
print()
context = pickWord(firstWordProbs)
print(context,end=" ")
for i in range(100):
    word = pickWord(model[context])
    print(word,end=" ")
    context = word
print()
print()



























