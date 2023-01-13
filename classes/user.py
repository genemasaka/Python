class User:
	
	def __init__(self, username, location, age, gender):
		self.username = username
		self.location = location
		self.age = age
		self.gender = gender
	
	def user_list(self):
		user_profile = {'id' : self.username, 'location' : self.location, 'age' : self.age, 'gender' : self.gender}
		users = []
		users.append(user_profile)
		return users

class Admin(User):
	def __init__(self, username, location, age, gender):
		super().__init__(username, location, age, gender)
		self.privilages = ['can deplatform user', 'can delete post', 'can read messages']

	def show_privilages(self):
		print('The following privilages are held by the Admin')
		for privilage in self.privilages:
			print(privilage.title())

user = User('panyako', 'kilimani', '24', 'male')
print(user.user_list())
privilage = Admin('panyako', 'kilimani', '24', 'male')
privilage.show_privilages()