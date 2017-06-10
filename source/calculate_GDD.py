import argparse
import os
import pandas as pd
import numpy as np
from save_data_as_csv import save_data_as_csv

# Checking GDD values. If the value < 0 than value = 0. 
def checkGDD(values):
    GDD = []
    item = 0
    for i in values:
        if i >= 0:
            item += i
        GDD.append(item)
    return GDD

# Taking the complete DataFrame and calculating GDD. Than add the GDD values as a new column. 
def calculate_GDD(Data, baseTemp):
    Data['GDD'] = ((Data['Max Temp (Â°C)'] + Data['Min Temp (Â°C)'])/2)- baseTemp 
    return Data
	
def Main():
    # Taking the arguments from command line. 
    parser = argparse.ArgumentParser()
    parser.add_argument("baseTemp", help="Please set base temperature.", type=int)
    parser.add_argument("-st", dest="stationId", nargs = '*', help="Please provide a list of station Id.")
    parser.add_argument("-ct", dest="cityName", nargs = '*', help="Please provide a list of city names corresponding to stations.")
	
    args = parser.parse_args()
	
    for i in range(len(args.stationId)):
    	# Reading the data from downloaded .csv files. 
        CurrentPath = os.getcwd()
        FilePath= (CurrentPath+'/DataFiles/GDD_Data_'+args.cityName[i]+'.csv')
        Daily_Data = pd.read_csv(FilePath, encoding = 'ISO-8859-1', delimiter = ',' ,skiprows=0)
        Data = pd.DataFrame(Daily_Data, columns = ['Date/Time','Max Temp (Â°C)', 'Min Temp (Â°C)'])
        Data.replace('', np.nan, inplace = True)
        Data = Data.dropna()
	
	# Calling calculate_GDD function to calculate GDD
        GDD_Data = calculate_GDD(Data, args.baseTemp)
        
        # Saving back the updated DataFrame to .csv file. 
        save_data_as_csv(GDD_Data, FilePath)
		
if __name__ == '__main__':
    Main()
