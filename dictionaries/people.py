person1 = {'first_name': 'josphat', 'last_name' : 'mbugua', 'age': '32', 'city' : 'nairobi'}
person2 = {'first_name' : 'mary', 'last_name' : 'magoma', 'age' : '67', 'city' : 'kisii'}
person3 =  {'first_name' : 'philip', 'last_name' : 'baya', 'age' : '27', 'city' : 'mombasa'}

people = [person1, person2, person3]

for person in people:
	for key, value in person.items():
		print(f'{key} : {value}')