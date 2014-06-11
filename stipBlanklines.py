import fileinput
cur = []
for line in fileinput.FileInput("./devtest.actual"):
    if line != "\n":
    	cur.append(line.split()[1])
    elif cur != []:
    	print cur
    	cur = []