#!/usr/bin/Python
import wget
import numpy as np
import pandas as pd
import time as time
import math
import os
import argparse
from save_data_as_csv import save_data_as_csv

list_years = range(2012,2018)
dict_cities = {'ST JOHNS':'48871', 'HALIFAX':'50620', 'TORONTO':'48549', 'VANCOUVER':'888'}

url_template = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={0}&Year={1}&Month=12&Day=1&timeframe=2&submit=Download+Data'

for key in dict_cities.keys():
    for year in list_years:
        filename = wget.download(url_template.format(dict_cities[key],year))
        os.rename(filename, key+'_'+str(year))
        time.sleep( 1 )

  
File_Data = pd.read_csv(filename, encoding = 'ISO-8859-1', delimiter = ',', skiprows=25)
Data = pd.DataFrame(File_Data, columns = ['Date/Time', 'Max Temp (°C)', 'Min Temp (°C)'])
Data.replace('', np.nan, inplace = True)
Data = Data.dropna()       
startYear = startYear + 1
currentpath = os.getcwd()
filepath= (currentpath+'/DataFiles/GDD_Data_'+cityName+'.csv')
        
# Saving back the updated DataFrame to .csv file. 
save_data_as_csv(Data, filepath)
# Removing unnecessary downloaded files. 
os.remove(filename)
