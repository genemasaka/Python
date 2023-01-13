def greet_users(names):
	"""Loops through list of user names and greets each user"""
	for name in names:
		print(f'Hello {name.title()}')


usernames = ['ivy', 'samir', 'kayla']
greet_users(usernames)