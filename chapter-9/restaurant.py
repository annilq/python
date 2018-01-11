class Restaurant():
	"""docstring for User"""
	def __init__(self, restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served=0;
	def describe_restaurant(self):
		print("the restaurant_name is:",self.restaurant_name);
		print("the cuisine_type is:",self.cuisine_type);
	def open_restaurant(self):
		print("the my_restaurant is open");
	def set_number_served(self,num):
		self.number_served=num;
	def get_number_served(self):
		print("number_served:",self.number_served)
	def increment_number_served(self,incre_num):
		self.number_served+=incre_num;

my_restaurant=Restaurant("hha",27);
my_restaurant.set_number_served(1);
my_restaurant.get_number_served();
my_restaurant.set_number_served(2);
my_restaurant.get_number_served();
my_restaurant.increment_number_served(5);
my_restaurant.get_number_served();

class IceCreamStand(Restaurant):
	"""docstring for IceCreamStand"""
	def __init__(self, restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = ["apple","milk","orange"]
	def showIceFlavors(self):
		print(self.flavors)
my_ice=IceCreamStand("annilq's","drinks")
my_ice.showIceFlavors()