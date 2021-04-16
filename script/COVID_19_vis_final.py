import pygal 
import csv
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS, RotateStyle, Style
from pygal.maps.world import COUNTRIES, World 
from datetime import date, timedelta
from country_codes import get_country_code
# import cairosvg
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
		if row[3] == str(date.today() - timedelta(1)):
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
COVID_rates_3 = [country for country in COVID_rates if country['value'][1] < 10000000]
COVID_rates_4 = [country for country in COVID_rates if country['value'][1] < 100000000]
COVID_rates_5 = [country for country in COVID_rates if country['value'][1] >= 100000000]

customstyle = Style(colors=('#008000', '#FFFF00', '#FF9633', '#FF0000', '#800080' ))

wm_style = RotateStyle('#336699', step=5) 
wm = World(style = customstyle)
wm.add('< 100,000', COVID_rates_1)
wm.add('< 1,000,000', COVID_rates_2)
wm.add('< 10,000,000', COVID_rates_3)
wm.add('< 100,000,000', COVID_rates_4)
if len(COVID_rates_5) > 1:
    wm.add('>= 100,000,000', COVID_rates_5)
# wm.title='Total COVID cases by country as of ' + str(date.today() - timedelta(1))
wm.title='Total COVID cases by country as of ' + str(date.today() - timedelta(1))
wm.render_to_file('COVID_vis_final.svg')
# cairosvg.svg2png(url='COVID_vis_final.svg', write_to="'COVID_vis_final.png")
