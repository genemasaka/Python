company = ['rachel', 'sam', 'tina', 'seth', 'wayne', 'cindy']

owners = company[0:2]
for owner in owners:
	print(f'{owner} is an owner of the company\n')

employees = company[2:]
for employee in employees:
	print(f'{employee} is an employee of the company\n')