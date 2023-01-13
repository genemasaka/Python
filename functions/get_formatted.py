def get_formatted(first_name, last_name):
	fomat = f'{first_name.title()} {last_name.title()}'
	return fomat

formatted = get_formatted('nipsey', 'hussle')
print(formatted)