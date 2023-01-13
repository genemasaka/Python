watch_collection = ['patek', 'rolex', 'alange', 'constantine', 'richard']
print(watch_collection)
print(sorted(watch_collection))
watch_collection.sort()
print(watch_collection)
watch_collection.sort(reverse = True)
print(watch_collection)
print(len(watch_collection))
watch_collection.insert(3, 'audemars')
print(watch_collection)
print(f'\nMy favorite watch brand is {watch_collection[-1]} & sohn') #index -1 gives last item in list

for watch in watch_collection:
	print(watch)