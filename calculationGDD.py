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


#keeping all the values of GDD are higher than zero
def sure_Data(data):
    GDD = []
    for i in data:
        if i >= 0:
           GDD.append(i)
        else:
           GDD.append(0)
    return GDD

#set the min temperature is equal to or higher than base Temperature
def min_temp(data):
    minimalT = []
    for i in data:
         if i<=10:
            minimalT.append(10)
         else:
            minimalT.append(i)
    return minimalT
        

#calculating the values of GDD
def calculate_GDD(annual):
    baseT=10
    annual['MinTemp(°C)']= min_temp(annual['Min Temp (°C)'])
    annual['GDD'] = ((annual['Max Temp (°C)'] + annual['MinTemp(°C)'])/2) -10
    annual['GDD'] = sure_Data(annual['GDD'])
    return annual

#accumulating GDD 

#obtain the data
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
    if os.path.exists(plotpath):
        shutil.rmtree(plotpath)
    run()
