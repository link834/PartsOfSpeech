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
 
contextconst = ['','']

firstWordProbs = {}
model = {}

total_lines = len(trainingdata)
prob_constant = float(1.0 / float(total_lines))
#prob_constant = 1

for line in trainingdata:
	context = contextconst
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

		#print(context)
		context = (context + [word])[1:]
#		if(str(context) == str(['','But'])):
#			print(context)

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
startWord = pickWord(firstWordProbs)
context = (contextconst + [startWord])[1:]
print(startWord,end=" ")
for i in range(100):
	word = ""
	if(str(context) in model):
		word = pickWord(model[str(context)])
	else:
		pass
	print(word,end=" ")
	context = (context + [word])[1:]
print()
print()



























