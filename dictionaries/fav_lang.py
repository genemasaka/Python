fav_lang = {'nehru' : ['go', 'javascript'], 'baraka' : ['python', 'ruby']}

for person, langs in fav_lang.items():
	print(f"{person.title()}'s favorite languages are:")
	languages = fav_lang[person]
	for language in languages:
		print(f'{language}\n')