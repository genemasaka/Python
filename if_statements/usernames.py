current_users = ['sam', 'jim', 'ivy', 'kat', 'tim']
new_users = ['max', 'will', 'IVY', 'Jim',]

#uses list comprehension to convert all strings in new_users to lowercase
new_users_lowercase = [user.lower() for user in new_users]

for username in new_users_lowercase:
	if username in current_users:
		print(f'{username.title()} already exists. Pick new username')
	if username not in current_users:
		print(f'{username.title()} is valid. Welcome onboard!')