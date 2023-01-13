users = ['samba29', 'julie_slim', 'admin', 'bambi', 'trav']

if users:
	for user in users:
		if user == 'admin':
			print(f'Hello {user.title()}, would you like to see status report?\n')
		else:
			print(f'Hello {user.title()}, welcome back!\n')
else:
	print('We need to find some users!')