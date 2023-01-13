#optimum trade conditions
break_previous_high = True
SMA = 54.3
volume = 'high'
#list that stores optimum conditions
optimum_conditions = [break_previous_high, SMA, volume]
#loops through optimum_conditions and checks if its suitable to place a trade
for condition in optimum_conditions:
	if break_previous_high != False and SMA > 50 and volume != 'high':
		print('Optimum conditions for placing a trade are present')
	else:
		print('Placing a trade is not advisable')