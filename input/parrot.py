prompt = 'Tell me something and I will repeat it back to you'
prompt += '\nEnter "quit" to exit\n'
message = ''
active = True
while active:
	message = input(prompt)
	if message == 'quit':
		break
	else:
		print(message)