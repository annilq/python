class User():
	"""docstring for User"""
	def __init__(self, first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = self.first_name+self.last_name 
		self.login_attempts=0;
	def describe_user(self):
		print(self.first_name,self,last_name)
	def greet_user(self):
		print("hello ",self.full_name.title())
	def increment_login_attempts(self):
		self.login_attempts+=1
	def reset_login_attempts(self):
		self.login_attempts=0
		
user=User("liu","qiang")
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
