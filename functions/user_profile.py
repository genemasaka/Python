def build_profile(first, last, **kargs):
	kargs['first_name'] = first
	kargs['last_name'] = last
	for key, value in kargs.items():
		print(f'{key.title()} : {value.title()}')

build_profile('masaka', 'gene', age = '25', location = 'nairobi')