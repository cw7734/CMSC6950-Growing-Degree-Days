#!/usr/bin/Python
import wget
import os, sys, stat
import time
import pandas as pd
import numpy as np
import argparse
import shutil

list_years = range(2012,2018)
dict_cities = {'ST JOHNS':'48871', 'HALIFAX':'50620', 'TORONTO':'48549', 'VANCOUVER':'888'}

url_template = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={0}&Year={1}&Month=12&Day=1&timeframe=2&submit=Download+Data'

filepath= (os.getcwd()+'/DataFiles/')

def download_data(years = list_years,cities = dict_cities):
	for key in dict_cities.keys():
    		for year in list_years:
        		filename = wget.download(url_template.format(dict_cities[key],year))
        		File_Data = pd.read_csv(filename, encoding = 'utf-8', delimiter = ',', skiprows=25)
        		Data = pd.DataFrame(File_Data, columns = ['Date/Time', 'Max Temp (°C)', 'Min Temp (°C)'])
        		Data.replace('', np.nan, inplace = True)
        		Data = Data.dropna()
        		GDDfilename = filepath+'GDD_Data_'+key+'_'+str(year)+'.csv'
        		with open(GDDfilename, 'w+') as datafile:
            			Data.to_csv(GDDfilename, sep=',', encoding='utf-8')
        		os.remove(filename)

def Main():
        if os.path.exists(filepath):
            shutil.rmtree(filepath)
        os.makedirs(filepath)
        download_data()

if __name__ == '__main__':
       Main() 

