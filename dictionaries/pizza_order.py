options = input('Please select your preferred topping\n')
crust = input('Enter preferred crust\n')	
toppings = []
toppings.append(options)
print(toppings)
pizza = {'crust' : crust, 'add' : toppings}
crust = pizza['crust']
print(f'You ordered a {crust}-crust pizza with the following toppings:\n')
for topping in pizza['add']:
	print(topping)
