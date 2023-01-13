class Car:
	
	maker = input('Please enter car manufacturer:(enter "q" to exit\n')
	model = input('Please enter car model:')
		
	
	def __init__(self, maker = maker, model = model):
		self.maker = maker
		self.model = model

	def service_alert(self):
		needs_service = True
		if needs_service != False:
			alert = f'Your {self.maker.title()} {self.model.title()} is in need of service'
		else:
			alert = f'Your {self.maker.title()} {self.model.title()} is in good condition'	

		return alert

	def tyre_pressure(self):
		front_left = 34
		front_right = 32
		back_left = 36
		back_right = 36

		if front_left or front_right or back_left or back_right < 33:
			alert = f'Tyre pressure too low. Please check and adjust the tyre pressure on your {self.maker.title()} {self.model.title()}'
		elif front_left or front_right or back_left or back_right > 36:
			alert = f'Tyre pressure too high. Please check and adjust the tyre pressure on your {self.maker.title()} {self.model.title()}'

		return alert

class ElectricCar(Car):
	def __init__(self, maker, model):
		super().__init__(maker, model)
		self.battery_size = 75
	
	def batt_info(self):
		print(f'My {self.maker} {self.model} has a {self.battery_size}khw battery')

	def get_range(self):
		if self.battery_size == 75:
			ev_range = 215
		if self.battery_size == 100:
			ev_range = 310
		
		return ev_range

	def upgrade_batt(self):
		if self.battery_size < 100:
			self.battery_size = 100


my_car = Car()
print(my_car.tyre_pressure())
print(my_car.service_alert())
ev = ElectricCar('tesla', 'model x')
print(ev.tyre_pressure())
ev.batt_info()
print(ev.get_range())
ev.upgrade_batt()
print(ev.get_range())

