from random import randint

class Die():
	"""docstring for Die"""
	def __init__(self, sides=6):
		super().__init__()
		self.sides = sides
	def roll_die(self):
		print("the side is",randint(1,self.sides))
die=Die(20)
die.roll_die()