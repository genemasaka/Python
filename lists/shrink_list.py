#created list variable with names of guests
guests = ['Nipsey Hussle', 'Steve Jobs', 'Jesus Christ']

#changed the guest at index 2
guests[2] = 'Sean Carter'

#added guests to the list using insert() and append()
guests.insert(0, 'Naval')
guests.insert(1, 'Tupac Shakur')
guests.append('Virgil Abloh')

#string that prints how many people can be invited to dinner
print('Only two guests can be invited to the dinner\n')

#removes guests from lists using pop(n) and sends a message to them
uninvited1 = guests.pop(5)
print(f'{uninvited1}, you have been uninvited to the dinner\n')
uninvited2 = guests.pop(4)
print(f'{uninvited2}, you have been uninvited to the dinner\n')
uninvited3 = guests.pop(3)
print(f'{uninvited3}, you have been uninvited to the dinner\n')
uninvited4 = guests.pop(2)
print(f'{uninvited4}, you have been uninvited to the dinner\n')


#prints guests who are still invited to the dinner
print(f'Dear {guests[0]}, you are still invited to dinner with me. I would like to pick your brain on life.\n')
print(f'Dear {guests[1]}, you are still invited to dinner with me. I would like to pick your brain on life.\n')

#removes the remaining guests
del guests[1]
del guests[0]
#prints empty list
print(guests)