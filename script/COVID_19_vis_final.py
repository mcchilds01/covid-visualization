import pygal 
import csv
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS, RotateStyle
from pygal.maps.world import COUNTRIES, World 
from datetime import date, timedelta
from country_codes import get_country_code
from createDict import createDict

filename = 'owid-covid-data.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	COVID_rates = []
	for row in reader:
		# This allows the program to pull the most recent data from OWID, provided the CSV file is updated
		# if row[3] == str(date.today() - timedelta(1)):
		# For the purpose of testing against the data in this repo, changed to this:
		if row[3] == '2020-12-27':
			code = get_country_code(row[2])
			if code: 
				COVID_rates.append(createDict(code, row[2], row[4]))
			if row[2] == 'Russia':
				# The pygal COUNTRIES library does not recognize "Russia" as the country name (along with the common name of several other countries)
				# Adding Russia manually to COVID_rates
				code = 'ru'
				COVID_rates.append(createDict(code, row[2], row[4]))


COVID_rates_1 = [i for i in COVID_rates if i['value'][1] < 100000]
COVID_rates_2 = [country for country in COVID_rates if country['value'][1] < 1000000] 
COVID_rates_3 = [country for country in COVID_rates if country['value'][1] >= 1000000]

wm_style = RotateStyle('#336699', base_style = LCS)
wm = World(style = wm_style)
wm.add('< 100000', COVID_rates_1)
wm.add('< 1000000', COVID_rates_2)
wm.add('>= 1 mil', COVID_rates_3)
# wm.title='Total COVID cases by country as of ' + str(date.today() - timedelta(1))
wm.title='Total COVID cases by country as of 2020-12-27'
wm.render_to_file('COVID_vis_final.svg')
