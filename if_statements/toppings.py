#created list of available toppings
available_toppings = ['mushrooms', 'garlic', 'green pepper', 'peperoni']

#prints list of available toppings for the user
#maybe add functionality where usere can add more toppings?
print("Here's a list of the available toppings:")
for topping in available_toppings:
	print(f'{topping.title()}')

#created list of requested toppings
requested_toppings = ['peperoni', 'garlic', 'cheese']

#loops through requested toppings and checks if present in available toppings
#tells user which requested topping is not available and adds present toppings
#to pizza
for requested_topping in requested_toppings:
	if requested_topping not in available_toppings:
		print(f"Sorry we're out of {requested_topping.title()}.\n")
	if requested_topping in available_toppings:
		print(f'Adding {requested_topping.title()} to your pizza...\n')

#checks if pizza is done and alerts user
pizza_done = True
if pizza_done != False:
	print('Your pizza is ready!')