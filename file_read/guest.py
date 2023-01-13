
active = True
file = 'guest.txt'
guest_list = []
while active:
	name = input('Please enter guest name:\n')
	guest_list.append(name)

	with open(file, 'a') as file_object:
		name = f'{name}\n'
		file_object.write(name)
			

	repeat = input('Would you like to add another guest(yes/no)\n')

	if repeat == 'no':
		active = False

for guest in guest_list:
	print(f'Hello {guest}, welcome to the event!')