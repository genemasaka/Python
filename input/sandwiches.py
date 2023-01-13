sandwich_order = ['pastrami', 'blt', 'pastrami', 'tuna', 'vegan', 'pastrami']
finished_sandwich = []

print('Sorry the deli has run out of pastrami')

while sandwich_order:
	for order in sandwich_order:
		if order == 'pastrami':
			sandwich_order.remove(order)

	finished = sandwich_order.pop()
	print(f'I made your {finished} sandwich')
	finished_sandwich.append(finished)

print(finished_sandwich)