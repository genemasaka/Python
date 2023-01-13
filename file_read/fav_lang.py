active = True
file = 'fav_lang.txt'
while active:
	name = input('Type in name:\n')
	fav_lang = input('Type in favorite language:\n')

	result = f'{name} : {fav_lang}\n'

	with open(file, 'a') as file_object:
		file_object.write(result)

	repeat = input('Add more people?(yes/no):\n')

	if repeat == 'no':
		active = False

	print(result)

