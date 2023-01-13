nehru_favorites = ['kodak black', 'nba youngboy', 'kendrick lamar']

eugene_favorites = nehru_favorites[:]

print(eugene_favorites)

eugene_favorites.append('meek mill')
for favorite in eugene_favorites:
	print(favorite)

print(f'\nThe first three items in the list are:')
for first_three in nehru_favorites[0:]:
	print(first_three)

print('\nThe middle items in the list are:')
for middle_items in eugene_favorites[1:3]:
	print(middle_items)

print('\nThe last three items in the list are:')
for last_three in eugene_favorites[1:]:
	print(last_three)