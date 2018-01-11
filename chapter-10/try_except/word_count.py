filenames=["division.py","file_error.py","unfound.txt"]
def word_count(filename):
	try:
		with open(filename) as fileObj:
			content=fileObj.read()
			print(filename,"has",len(content.split()),"words")
	except FileNotFoundError as e:
		print(filename,"not found")

for filename in filenames:
	word_count(filename)