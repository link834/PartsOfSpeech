import sys
from math import *
from HMM import HMM

def viterbi(sentence, hmm):
	n = len(sentence)

	def K(k):
		if k in (-1, 0):
			return ["*"]
		else:
			return hmm.tags()

	observations = [""] + sentence
	actualStates = [""] * (n+1)

	def threeProb(w,u,v):
		return hmm.threeGramProb((u,v,w))
	def emissionProb(x,u):
		return hmm.emissionProbability(x,u)

	pi = {}
	pi[0, "*", "*"] = 1.0
	backPointers = {}

	for k in range(1, n+1):
		for u in K(k-1):
			for v in K(k):
				backPointers[k,u,v], pi[k,u,v] = argmax([(word, pi[k-1, word, u] * threeProb(v, word, u) * emissionProb(observations[k], v)) for word in K(k-2)])

	(actualStates[n-1], actualStates[n]), score = argmax([((u,v), pi[n, u, v] * threeProb("STOP", u, v)) for u in K(n-1) for v in K(n)])
	for k in range(n-2, 0, -1):
		actualStates[k] = backPointers[k+2, actualStates[k+1], actualStates[k+2]]
	actualStates[0] = "*"
	scores = [pi[i, actualStates[i-1], actualStates[1]] for i in range(1,n)]

	return actualStates[1: n+1], scores + [score]

def argmax(listOfPairs):
	def element_1(x):
		return x[1]
	return max(listOfPairs, key = element_1)

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
		posTagging, scores = viterbi(s, hmm)
		printPOSs(s, posTagging)

	

if __name__ == "__main__":
	main(open(sys.argv[1]), open(sys.argv[2]))

