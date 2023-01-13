def order(*sandwich):
	print('You have ordered the following:')
	for item in sandwich:
		print(f'{item.title()} sandwich')

order('blt', 'ham and cheese', 'chicken')