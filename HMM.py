from __future__ import division
import sys
from math import *

class HMM:
	def __init__(self, f):
	    self.words = {}
	    self.nGrams = {1 : {}, 2 : {}, 3 : {}}
	    self.wordCounts = {}
	    self.numStarts = 0
	    for line in f:
			tupple = line.strip().split()
			count = int(tupple[0])
			posNgram = tuple(tupple[2:])
			if tupple[1] == "1-G":
				self.nGrams[1][posNgram[0]] = count
				self.numStarts += count
			elif tupple[1] == "2-G":
				self.nGrams[2][posNgram] = count
			elif tupple[1] == "3-G":
				self.nGrams[3][posNgram] = count
			elif tupple[1] == "POS":
				self.words[posNgram] = count
				self.wordCounts.setdefault(posNgram[1],0)
				self.wordCounts[posNgram[1]] += count

	def tags(self):
		return self.nGrams[1].keys()

	def startProb(self, pos):
		return self.nGrams[1][pos]/self.numStarts

	def wordCount(self, word):
		return self.wordCounts.get(word, 0.0)

	def threeGramProb(self, threeGram):
		twoGram = threeGram[:-1]
		try:
			return self.nGrams[3].get(threeGram, 0.0) / self.nGrams[2][twoGram]
		except KeyError:
			return 0.001

	def twoGramProb(self, twoGram):
		oneGram = twoGram[0]
		try:
			return self.nGrams[2].get(twoGram, 0.0) / self.nGrams[1][oneGram]
		except KeyError:
			return 0.001

	def emissionProbability(self, word, pos):
		if pos in ["*", "STOP"]:
			return 0.0
		newWord = self.replaceWord(word)
		return self.words.get((pos, newWord), 0.0) / self.nGrams[1][pos]

	def replaceWord(self, word):
		if self.wordCount(word) < 2:
			return "blank"
		else:
			return word