import json
filename="username.json"
def get_stored_user():
	try:
		with open(filename) as fileObj:
			username=json.load(fileObj)
			return username
	except Exception as e:
		return None

def get_new_user():
	username=input("what is your name:")
	with open(filename,"w") as fileObj:
		json.dump(username,fileObj)

def greet_user():
	username=get_stored_user()
	if username:
		user=input("are you mr "+username+"?y/n")
		if user=="y":
			print("welcome back,",username)
		else:
			username=get_new_user()
			print("we will meet next time",username)
	else:
		username=get_new_user()
		print("we will meet next time",username)

greet_user()