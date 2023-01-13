responses = {}

polling_active = True

while polling_active:
	name = input('Please enter your name:')
	response = input('Which destination would you like to visit?')

	responses[name] = response

	proceed = input('Would you like someone else to participate in the poll? (yes/no):')

	if proceed == 'no':
		polling_active = False


for person, destination in responses.items():
	print(f'{person.title()} would like to visit {destination.title()}')