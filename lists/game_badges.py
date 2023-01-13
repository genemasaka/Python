user_1 = ['tactical', 'stealth', 'destroyer']

user_2 = user_1[:]

user_1.append('warrior')
user_2.append('explosives')

print('User 1 has the following badges:')
for badge in user_1:
	print(f'\n{badge.title()}')

print('User 2 has the following badges:')
for badge in user_2:
	print(f'\n{badge.title()}')