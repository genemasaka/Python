def cars(manufacturer, model, **kargs):
	kargs['maker'] = manufacturer
	kargs['model'] = model
	print(kargs)

cars('ferrari', '488 pista', engine = 'v8', color = 'forest green')