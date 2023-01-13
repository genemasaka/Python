def rent(no_bedrooms):
	rent = 0
	if no_bedrooms == 1:
		rent = 12000
	if no_bedrooms == 2:
		rent = 17000
	else:
		rent = 7000

	return(rent)

