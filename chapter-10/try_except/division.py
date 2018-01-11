print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
	first=input("first num:")
	if first=="q":
		break
	sec=input("sec num:")
	if sec=="q":
		break
	try:
		answer=int(first)/int(sec)
	except ZeroDivisionError as e:
		print("zero can't be division")
	else:
		print(answer)
