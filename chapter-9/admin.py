from user import User
class Privileges():
	"""docstring for Privileges"""
	def __init__(self):
		super().__init__()
		self.privileges = ["can add post","can delete post","can ban user"]
	def show_privileges(self):
		print("the admin ",self.privileges)

class Admin(User):
	"""docstring for Admin"""
	def __init__(self, first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = Privileges()
		
admin=Admin("liu","qiang")
admin.privileges.show_privileges()

