import sys
import re

def main(predicted, actual):
	# line = 1
	# correct = 0.0
	# total = 0.0
	# sentCorrect = 0.0
	# sentTotal = 0.0
	# for p in predicted:
	# 	a = actual.readline()
	# 	pList = p.split(',')
	# 	aList = a.split(',')
	# 	if pList == aList:
	# 		sentCorrect += 1
	# 	sentTotal += 1
	# 	if len(pList) != len(aList):
	# 		print str(line)
	# 	else:
	# 		for x in range(0, len(pList)):
	# 			if pList[x] == aList[x]:
	# 				correct +=1
	# 			total += 1
	# 	line+=1
	# print str(sentCorrect/sentTotal)
	# print str(correct/total)
	speech_parts = {}
	parts_list = []
	confusion_matrix = {}
	
	# create the title row for the parts of speech
	for a in actual:
		#alist = list(a)
		alist = re.findall(r'[\w"]+', a)
		#alist = a.split(',')
		p = predicted.readline()
		#plist = list(p)
		plist = re.findall(r'[\w"]+', p)
		#plist = p.split(',')
		
		if len(alist) != len(plist):
			continue
		
		for i in range(0, len(alist)):
			# put in speech_parts list
			if(alist[i] in speech_parts):
				speech_parts[alist[i]] += 1
			else:
				speech_parts[alist[i]] = 1
			# calc cell values
			if(plist[i] in confusion_matrix):
				if(alist[i] in confusion_matrix[plist[i]]):
					confusion_matrix[plist[i]][alist[i]] += 1
				else:
					confusion_matrix[plist[i]][alist[i]] = 1
			else:
				confusion_matrix[plist[i]] = {alist[i]: 1}
	
	for key in speech_parts:
		if(key != '\"'):
			parts_list.append(key)
	
	
	# write the results of the parts of speech
	f = open('confusion_matrix.csv', 'w')
	f.write('POS predicted(down) actual(top row)')
	f.write(parts_list[0])
	for part in parts_list:
		f.write("," + part)
	f.write("\n")
	for p_part in parts_list:
		f.write(p_part)
		for a_part in parts_list:
			if(p_part in confusion_matrix):
				if(a_part in confusion_matrix[p_part]):
					pass
				else:
					confusion_matrix[p_part][a_part] = 0
			else:
				confusion_matrix[p_part] = {a_part: 0}
				
			f.write("," + str(confusion_matrix[p_part][a_part]))
		f.write("\n")
		
	
	f.close()



	

if __name__ == "__main__":
	main(open(sys.argv[1]), open(sys.argv[2]))
