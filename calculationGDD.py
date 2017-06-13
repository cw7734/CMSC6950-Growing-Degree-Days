#!/usr/bin/Python
import os
import csv
import argparse
import pandas as pd
import numpy as np

plotpath = (os.getcwd()+'/Plot/')
filepath = (os.getcwd()+'/DataFiles/')

def get_allfiles():
     files = os.listdir(filepath)
     return files

#calculating the values of GDD
def calculate_GDD(annual):
    baseT=10
    annual['Min Temp (°C)']= [x if x > 10 else 10 for x in annual['Min Temp (°C)']] 
    annual['rGDD'] = ((annual['Max Temp (°C)'] + annual['Min Temp (°C)'])/2) -baseT
    annual['GDD'] = [x if x>0 else 0 for x in annual['rGDD']]
    annual['accGDD']=np.cumsum(annual['GDD'])
    del annual['rGDD']
    return annual


#obtain the data and calculate accumulate GDD
def parseData(data,infor):
   cityName = infor[0]
   start = infor[1]
   end = infor[2]
   list_years = list(range(int(start),int(end)+1))
   GDDfilename = filepath+'GDD_Value_'+cityName+'_'+start+'_'+end+'.csv'
   DataBuffer = []
   for year in list_years:
       annual = data[data['Date/Time'].str.contains(str(year))]
       df=calculate_GDD(annual)
       DataBuffer.append(df)
   with open(GDDfilename, 'w+') as datafile:
       Data = pd.concat(DataBuffer) 
       Data.to_csv(GDDfilename, sep=',', encoding='utf-8')
   
def run():
    files = get_allfiles()
    for element in files:
        Data = pd.read_csv(filepath+element, encoding = 'utf-8', index_col=0)
        placeInfo = element[:-4].split('_')[2:]
        parseData(Data,placeInfo)


if __name__=='__main__':
    run()
