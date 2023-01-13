def print_messages(messages, users, active):
	"""Prints messages stored in list 'messages' """
	for message in messages:
		for user in users:
			if user in active:
				print(f'{message} {user.title()}')

		queue = messages.pop()
		sent.append(queue)


def sent_messages(sent):
	print('\nThe following messages have been sent:')
	for item in sent:
		print(item)

messages = ['Welcome back', 'You have no new messages', '3 new friend requests for']
sent = []
users = ['ivy', 'slim', 'rosey', 'zack']
active = ['ivy', 'zack']
print_messages(messages, users, active)
sent_messages(sent[:])