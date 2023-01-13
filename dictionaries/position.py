alien_0 = {'x-coordinate' : 0, 'y-coordinate': 25, 'speed': 'medium'}
print(alien_0['x-coordinate'])

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
	x_incriment = 1
elif alien_0['speed'] == 'medium':
	x_incriment = 2
else:
	x_incriment = 3

alien_0['x-coordinate'] = alien_0['x-coordinate'] + x_incriment

print(alien_0['x-coordinate'])