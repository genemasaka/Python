def print_names(handle, *names):
	for name in names:
		print(f'I see you {handle}{name.title()}. Welcome back!')

print_names('@', 'ivy', 'rosey', 'steph')