glossary = {
	'boolean' : 'either true or false value',
	'type' : 'the type of data eg integer',
	'list' : 'an array of indexed items',
	'if' : 'conditional statement that evaluates to true or false',
	}
glossary['set'] = 'data type that stores only unique items'
for key in glossary.keys():
	definition = glossary[key]
	print(f'{key.title()} : {definition}')