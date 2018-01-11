
def record_guest():
	quit=True
	while quit:
		name=input("what is your name:")
		if name=="quit":
			quit=False
		else:
			filename="guest.txt"
			with open(filename,"a") as fileObj:
				fileObj.write(name)
				fileObj.write("\n")
record_guest()

