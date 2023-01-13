rivers = {'tana' : 'kenya', 'mississippi' : 'USA', 'nile' : 'egypt'}

for river in rivers.keys():
	country = rivers[river]
	print(f'The {river.title()} runs through {country.title()}')

print('\nThe rivers mentioned above are:')
for key in rivers.keys():
	print(key.title())

print('\nThe countries mentioned above are:')
for value in rivers.values():
	print(value.title())