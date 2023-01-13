#created  empty list variable 'cubes'
#loops through range of numbers, consecutively raises each to power 3 and adds to cubes list
cubes = [value ** 3 for value in range(1, 11)]

#prints list
print(cubes)
#min() prints minimum number in list
print(min(cubes))
#max() prints maximum number in list
print(max(cubes))
#sum prints sum of elements in a list (ints or floats)
print(sum(cubes))