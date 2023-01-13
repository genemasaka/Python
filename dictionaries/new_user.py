name = 'frank spencer'
age = 28
city = 'nairobi'
occupation = 'conservationist'

user_info = {}

user_info['name'] = name
user_info['age'] = age
user_info['city'] = city
user_info['occupation'] = occupation
print('The new user information received is:\n')
for field, info in user_info.items():
	print(f'{field.title()} : {info}')

for key in user_info.keys():
	print(key)