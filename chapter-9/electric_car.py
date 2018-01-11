from car import Car

class Battery():
	"""docstring for Battery"""
	def __init__(self):
		super().__init__()
		self.battery_size = 70
	def get_range(self):
 		"""打印一条消息，指出电瓶的续航里程"""
 		if self.battery_size == 70:
 			range = 240
 		elif self.battery_size == 85:
 			range = 270
 		message = "This car can go approximately " + str(range)
 		message += " miles on a full charge."
 		print(message)

class ElectricCar(Car):
	"""docstring for ElectricCar"""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery =Battery()
	def describe_battery(self):
		print("my_electricCar's battery_size is",self.battery.battery_size)

	def upgrade_battery(self):
		if self.battery.battery_size!=85:
			self.battery.battery_size=85

my_electricCar=ElectricCar("tesla","aa",2016);
my_electricCar.battery.get_range()
my_electricCar.upgrade_battery()
my_electricCar.battery.get_range()
