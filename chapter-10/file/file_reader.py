with open("learn_python.txt") as fileObj:
	content=fileObj.read()
	print(content)

with open("learn_python.txt") as fileObj:
	for line in fileObj:
		print(line.rstrip())

with open("learn_python.txt") as fileObj:
	lines=fileObj.readlines()

for line in lines:
	print(line.rstrip().replace("python","html"))
