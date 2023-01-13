favorite_places = {'tracy' : ['zanzibar', 'jinja'], 'wanja' : ['qatar', 'maldives']}
for keys, values in favorite_places.items():
	print(f"{keys.title()}'s favorite places are:")
	
	for place in values:
		print(f"{place.title()}")