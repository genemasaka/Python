import rent
i = 1

while i < 3:
	first_name = input('Enter first name:\n')
	last_name = input('Enter last name:\n')
	iD = input('Enter id:\n')
	no_bedrooms = int(input('Enter no of bedrooms:\n'))
	old_water_mtr_reading = 7
	current_water_mtr_reading = input('Enter current meter reading:')
	garbage_fee = 200
	tenant = {}
	house_no = input('Enter house no:')

	tenant['first_name'] = first_name
	tenant['last_name'] = last_name
	tenant['id'] = iD
	tenant['no_bedrooms'] = no_bedrooms
	tenant['old_water_mtr_reading'] = old_water_mtr_reading
	tenant['current_water_mtr_reading'] = int(current_water_mtr_reading)
	tenant['garbage_fee'] = garbage_fee

	tenament = []
	tenament.append(tenant.copy())

	i += 1


print(f'{tenament}\n')

for house, tenant in tenament.items():
	for info, value in tenant.items():
		if info == 'old_water_mtr_reading':
			old_reading = value
		if info == 'current_water_mtr_reading':
			current_reading = value

rent = rent.rent(no_bedrooms)

water_bill = (current_reading - old_reading) * 140
total_owed = rent + garbage_fee + water_bill

print(f"""Dear {first_name.title()}, your water bill is ksh{water_bill}, your 
garbage collection fee is ksh{garbage_fee} and rent 
is ksh{rent}, for a total of ksh{total_owed} owed
this month""")




