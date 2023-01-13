#range() method prints the range of numbers its given as an argument
#when printing a range of numbers the last number in the range is not included i.e 7
#giving the range() method a single argument will print 0 up to the number given 
for number in range(1, 7):
	print(number)

for number in range(4):
	print(number)
#list() function puts the numbers in the range in a list
no_list = list(range(1, 3))

for number in no_list:
	print(number)