prompt = 'Enter topping to be added to pizza'
prompt += '(Enter "quit" to exit)'
message = ''

while message != 'quit':
	message = input(prompt)

	if message == 'quit':
		break
	else:
		print(f'You added {message} to your pizza')