file = 'python_topics.txt'

with open(file) as file_object:
	topics = file_object.readlines()
	print(topics)

for topic in topics[:3]:
	edit = topic.replace('Python', 'Solidity')
	print(f'{edit.title()}')
