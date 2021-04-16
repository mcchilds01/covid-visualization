def createDict(code, country_name, rate):
    try: 
        return {
            'value': (code, int(float(rate))),
    		'label': code,
    		'xlink': 'https://www.google.com/search?q=covid+infection+rate+in+' + country_name,
		}
    except: 
        return { 
            'value': (code, 0),
            'label': code,
            'xlink': 'https://www.google.com/search?q=covid+infection+rate+in+' + country_name,
          }