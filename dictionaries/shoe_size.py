shoe_sizes = {
	'john' : 8,
	'eve' : 5,
	'fab' : 8,
	'eugo': 10,
	'stacy': 6,
}

for shoe_size in shoe_sizes:
	print(shoe_size)

eugo = shoe_sizes.get('eugo', 'Eugo shoe size not found')

print(eugo)