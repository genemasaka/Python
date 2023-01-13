menu = ('wings', 'burgers', 'steak', 'fries', 'pizza')

print('The restaurant offers the following dishes:\n')
for food in menu:
	print(food)


menu = ('wings', 'kebabs', 'oysters', 'fries', 'pizza')

print('The revised menu:\n')
for food in menu:
	print(f'{food}\n')

print(max(menu))