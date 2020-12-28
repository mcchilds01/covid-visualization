import pygal 
import csv
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS, RotateStyle
from pygal.maps.world import COUNTRIES, World 
from datetime import date, timedelta
from country_codes import get_country_code

filename = 'owid-covid-data.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	COVID_rates = []
	for row in reader:
		if row[3] == str(date.today() - timedelta(1)):
			code = get_country_code(row[2])
			if code: 
				covid_rate = { 
				'value': (code, int(float((row[4])))),
				'label': code,
				'xlink': 'https://www.google.com/search?q=covid+infection+rate+in+' + row[2],
				}
				COVID_rates.append(covid_rate)
			if row[2] == 'Russia':
				covid_rate = {
				'value': ('ru', int(float((row[4])))),
				'label': 'ru',
				'xlink': 'https://www.google.com/search?q=covid+infection+rate+in+Russia',
				}
				COVID_rates.append(covid_rate)


COVID_rates_1 = [i for i in COVID_rates if i['value'][1] < 100000]
COVID_rates_2 = [country for country in COVID_rates if country['value'][1] < 1000000] 
COVID_rates_3 = [country for country in COVID_rates if country['value'][1] >= 1000000]

wm_style = RotateStyle('#336699', base_style = LCS)
wm = World(style = wm_style)
wm.add('< 100000', COVID_rates_1)
wm.add('< 1000000', COVID_rates_2)
wm.add('>= 1 mil', COVID_rates_3)
wm.title='Total COVID cases by country'
wm.render_to_file('COVID_vis_final.svg')
