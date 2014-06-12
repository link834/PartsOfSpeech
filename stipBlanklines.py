import fileinput
cur = []
for line in fileinput.FileInput("./finalResults/finalSecondOrder.output3"):
    if line != "\n":
    	cur.append(line.split()[1])
    elif cur != []:
    	print cur
    	cur = []