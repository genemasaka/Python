favorite_numbers = {'gene' : 3, 'drake' : 6, 'youngboy': 38, 'tesla': 369}
#my original method
people = ['gene', 'drake', 'youngboy', 'tesla']
gene = favorite_numbers['gene']
drake = favorite_numbers['drake']
youngboy = favorite_numbers['youngboy']
tesla = favorite_numbers['tesla']
fav_num_list = [gene, drake, youngboy, tesla]

for person in people:
	for num in fav_num_list:
		if person == 'gene' and num == 3:
			print(f"{person.title()}'s favorite number is {num}")
		if person == 'drake' and num == 6:
			print(f"{person.title()}'s favorite number is {num}")
		if person == 'youngboy' and num == 38:
			print(f"{person.title()}'s favorite number is {num}")
		if person == 'tesla' and num == 369:
			print(f"{person.title()}'s favorite number is {num}")
#more concise way to loop through a string
for key, value in favorite_numbers.items():
	print(f'{key.title()} : {value}')
#gets keys in favorite_numbers	
for person in favorite_numbers.keys():
	print(person.title())