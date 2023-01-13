file = 'pi.txt'

with open(file) as file_object:
	lines = file_object.readlines()

birthday = input('Please enter your bithday:(ddmmyy)\n')

if birthday in lines:
	print('Your birtday is inn pi!')
else:
	print('Sorry your birthday is not in pi')