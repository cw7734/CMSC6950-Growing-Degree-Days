#!/usr/bin/Python
# coding=utf-8
import wget
import os, sys, stat
import time
import pandas as pd
import numpy as np
import getopt
import shutil

# basic information of years, cities and the url of download web, also give the file path

list_years = list(range(2013,2018))

dict_cities = {'ST JOHNS':'48871', 'HALIFAX':'50620', 'TORONTO':'48549', 'VANCOUVER':'888'}

url_template = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={0}&Year={1}&Month=12&Day=1&timeframe=2&submit=Download+Data'

filepath= (os.getcwd()+'/DataFiles/')

# define the auto download function which can download the data for the given years and cities automatically
def download_data(years = list_years,cities = dict_cities):
        for key in dict_cities.keys():
                GDDfilename = filepath+'GDD_Data_'+key+'_'+str(list_years[0])+'_'+str(list_years[-1])+'.csv'
                DataBuffer = []
                for year in list_years:
                        filename = wget.download(url_template.format(dict_cities[key],year))
                        File_Data = pd.read_csv(filename, encoding = 'utf-8', delimiter = ',', skiprows=25)
                        Data = pd.DataFrame(File_Data, columns = ['Date/Time', 'Max Temp (°C)', 'Min Temp (°C)'])
                        Data.replace('', np.nan, inplace = True)
                        Data = Data.dropna()
                        DataBuffer.append(Data)
                        os.remove(filename)
                with open(GDDfilename, 'w') as datafile:
                        Data = pd.concat(DataBuffer)                        
                        Data.to_csv(GDDfilename, sep=',', encoding='utf-8')


# define the main function to call the download_data function

def main():
        global list_years
        global dict_cities
        cities = []
        stations = []
        try:
                opts, args = getopt.getopt(sys.argv[1:], 'y:p:i:', ['year=', 'place=', 'id='])
        except getopt.GetoptError as e:
                print(e)
                sys.exit(2)
        for opt, arg in opts:
                if opt in ("-y", "--year"):
                     list_years = list(range(int(arg.split()[0]),int(arg.split()[1])+1))
                if opt in ("-p", "--place"):      
                     cities = arg.upper().split(',')
                if opt in ("-i", "--id"):      
                     stations = arg.upper().split()
        if len(cities)==len(stations) and len(cities)>0:
                dict_cities = dict(zip(cities, stations))

        download_data()

if __name__ == '__main__':
       main() 

