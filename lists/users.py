#created list variables with user info
user_1 = ['eugene masaka', '0758533458', '33969902']
user_2 = ['jermain muthusi', '0701235614', '36252678']
user_3 = ['thomas maghangha', '0722455567', '34427647']
user_4 = ['Ivy Dora', '0756432123', '32678725']
#created empty users list
users = []
#added user_n to users list
users.append(user_1)
users.append(user_2)
users.append(user_3)

#changed name of user third user
users[2][0] = 'Nehru Oneil'
#inserted new user in users
users.insert(2, user_4)
print(users)

for user in users:
	print(user[0].title())
for user in users:
	print(f'{user[0].title()}, you have been sucessfully logged in!')
	print(f'{user[0].title()}, you have a new message\n')

print('New app update available')