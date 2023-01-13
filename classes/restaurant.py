class Restaurant:
	"""defines a restaurant name and cuisine type"""
	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine
		self.number_served = 0
	
	def describe_restaurant(self):
		print(f'The {self.name.title()} is a restaurant serving {self.cuisine.title()} cuisine')
	
	def open_restaurant(self):
		active = True
		if active != False:
			print(f'The {self.name.title()} is open!')

	def set_number_served(self, served):
		self.number_served = served
		return self.number_served
	def increment_served(self, served):
		self.number_served += served
		return self.number_served

class IceCreamStand(Restaurant):

	def __init__(self, name, cuisine):
		super().__init__(name, cuisine)
		self.flavors = ['bubblegum', 'vanilla', 'chocolate', 'oreo']

	def print_flavors(self):
		print(f'{self.name} has an ice cream stand. The following ice cream flavors are available:')
		for flavor in self.flavors:
			print(flavor)

my_spot = Restaurant('Habesha', 'ethiopian')
new_spot = Restaurant('dijorno', 'italian')
print(my_spot.name)
print(my_spot.cuisine)
my_spot.describe_restaurant()
my_spot.open_restaurant() 
new_spot.describe_restaurant()
new_spot.open_restaurant()
print(my_spot.number_served)
print(my_spot.set_number_served(12))
print(my_spot.increment_served(21))
ice_cream = IceCreamStand('coldstone', 'confectionary')
ice_cream.print_flavors()

