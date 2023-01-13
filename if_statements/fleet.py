cars = ['urus', 'sf90', 'maybach s650', 'bently continental gt']
favorites = ['urus', 'sf90', 'bently continental gt']
for favorite in favorites:
	if favorite in cars:
		my_fav = favorite

product_line = my_fav[19:]

print(product_line)
print(f'My favorite car is the {my_fav[:18]} {product_line.upper()}')