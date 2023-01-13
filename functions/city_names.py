def city_country(city, country):
	combined = f'{city.title()}, {country.title()}'
	return combined
formatted = city_country('santiago', 'chile')
print(formatted)

formatted = city_country('nairobi', 'kenya')
print(formatted)