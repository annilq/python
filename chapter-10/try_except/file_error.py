filename="alice.txt"
try:
	with open(filename) as fileObj:
		contents=fileObj.read()
except FileNotFoundError:
	print("doesn't have this file")
