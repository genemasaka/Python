prompt = "Enter person's age\n(Enter quit to exit):"

age = ''

while age != 'quit':
	age = input(prompt)

	if age == 'quit':
		break
	
	age = int(age)

	if age < 3:
		price = 0
	elif age <= 12:
		price = 10
	elif age > 12:
		price = 15

	print(f'Your ticket will be ${price}')