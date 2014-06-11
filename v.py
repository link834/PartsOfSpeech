import sys
from math import *
from HMM import HMM

def viterbi(sentence, hmm):
	n = len(sentence)

	def partsOfSpeech(k):
		if k in (-1, 0):
			return ["*"]
		else:
			return hmm.tags()

	observations = sentence
	actualStates = [""] * (n)

	def threeProb(w0,w1,w2):
		return hmm.threeGramProb((u,v,w))
	def twoProb(w0,w1):
		return hmm.twoGramProb((w0,w1))
	def emissionProb(word,pos):
		return hmm.emissionProbability(word,pos)
	def startProb(pos):
		return hmm.startProb(pos)

	states = hmm.tags()
	V = [{}]
	path = {}

    # Initialize base cases (t == 0)
	for y in states:
		V[0][y] = startProb(y) * emissionProb(observations[0], y)
		path[y] = [y]
 
    # Run Viterbi for t > 0
	for t in range(1, len(observations)):
		V.append({})
		newpath = {}
 
		for y in states:
			(prob, state) = max((V[t-1][y0] * twoProb(y0,y) * emissionProb(observations[t],y), y0) for y0 in states)
			V[t][y] = prob
			newpath[y] = path[state] + [y]
 
        # Don't need to remember the old paths
		path = newpath
	n = 0           # if only one element is observed max is sought in the initialization values
	if len(observations)!=1:
		n = t
	# print_dptable(V)
	(prob, state) = max((V[n][y], y) for y in states)
	return (prob, path[state])

def print_dptable(V):
    s = "    " + " ".join(("%7d" % i) for i in range(len(V))) + "\n"
    for y in V[0]:
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += "\n"
    print(s)

def argmax(listOfPairs):
	def secondElement(x):
		return x[1]
	return max(listOfPairs, key = secondElement)

def readSentences(handle):
  sentence = []
  for l in handle:
    if l.strip():
      sentence.append(l.strip())
    else:
      yield sentence
      sentence = []

def printPOSs(sentence, pos):
	print "\n".join([w + " " + t for w, t in zip(sentence, pos)])

def main(input_file, hmm_file):
	hmm = HMM(hmm_file)
	for s in readSentences(input_file):
		if s != []:
			prob, path = viterbi(s, hmm)
			print path
		# printPOSs(s, posTagging)

	

if __name__ == "__main__":
	main(open(sys.argv[1]), open(sys.argv[2]))

