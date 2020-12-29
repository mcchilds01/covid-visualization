def createDict(code, country_name, rate):
	return { 
		'value': (code, int(float(rate))),
		'label': code,
		'xlink': 'https://www.google.com/search?q=covid+infection+rate+in+' + country_name,
		}