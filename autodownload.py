#!/usr/bin/Python
import wget
import os
import time

list_years = range(2012,2018)
dict_cities = {'ST JOHNS':'48871', 'HALIFAX':'50620', 'TORONTO':'48549', 'VANCOUVER':'888'}

url_template = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={0}&Year={1}&Month=12&Day=1&timeframe=2&submit=Download+Data'

for key in dict_cities.keys():
    for year in list_years:
        filename = wget.download(url_template.format(dict_cities[key],year))
        os.rename(filename, key+'_'+str(year))
        time.sleep( 1 )

  

