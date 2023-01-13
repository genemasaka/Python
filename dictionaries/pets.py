pet_1 = {'type' : 'dog', 'owner' : 'tim'}
pet_2 = {'type' : 'snake', 'owner' : 'rhino'}

pets = [pet_1, pet_2]

for pet in pets:
	for key, value in pet.items():
		print(f'{key} : {value}\n')
