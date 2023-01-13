def printing_models(unprinted, completed):
	while unprinted:
		current = unprinted.pop()
		print(f'{current} is being printed...')
		completed.append(current)

def finished(completed):
	for item in completed:
		print(f'{item} has finished printing')


unprinted = ['cv', 'passport', 'kra return']
completed = []

