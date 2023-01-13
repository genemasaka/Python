#for value in range(1, 1000001):
	#print(value)

numbers = list(range(1, 1000001))

smallest = min(numbers)
largest = max(numbers)
total = sum(numbers)
print(smallest)
print(largest)
print(total)

threes = [value * 3 for value in range(1, 10)]
print(f'{threes[0:4]} has been multiplied by 3')