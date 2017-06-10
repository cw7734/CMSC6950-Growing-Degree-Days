import wget
import numpy as np
import pandas as pd
import time as time
import math
import os
import argparse
from save_data_as_csv import save_data_as_csv

# Downloading the weather historical data from web
def download_data(startYear, endYear, stationId, cityName):
    while (startYear <= endYear):
        url = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID='+str(stationId)+'&Year='+str(startYear)+'&Month=12&Day=31&timeframe=2&submit= Download+Data'
        try:
            filename = wget.download(url)
        except:
            raise ValueError("Downloading file is failed!!!")
        try:
            File_Data = pd.read_csv(filename, encoding = 'utf-8', delimiter = ',', skiprows=25)
        except Exception as e:
            print("Error in Reading", FilePath)
            print(e)
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
 
def Main():
    # Taking the arguments from command line. 
    parser = argparse.ArgumentParser()
    parser.add_argument("startYear", help="Please insert start year for weather history data.", type=int)
    parser.add_argument("endYear", help="Please insert end year for weather history data.", type=int)
    parser.add_argument("-st", dest="stationId", nargs = '*', help="Please provide a list of station Id.")
    parser.add_argument("-ct", dest="cityName", nargs = '*', help="Please provide a list of city names corresponding to stations.")
	
    args = parser.parse_args()
	
    for i in range(len(args.stationId)):
        download_data(args.startYear, args.endYear, args.stationId[i], args.cityName[i])
		
if __name__ == '__main__':
    Main()
