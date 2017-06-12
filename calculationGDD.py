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


#Find the accumulated GDD.
def sure_Data(data):
    GDD = []
    item = 0
    for i in data:
        if i >= 0:
            item += i
        GDD.append(item)
    return GDD

#If the T_min is less than T_base, then set T_min=T_base by definition of calculating GDD.
def min_temp(data):
    minimalT = []
    for i in data:
         if i<=10:
            minimalT.append(10)
         else:
            minimalT.append(i)
    return minimalT
        

#calculating the values of GDD using the formula: GDD=(T_max+T_min)/2-T_base(if T_min<T_base, then set T_min=T_base).
def calculate_GDD(annual):
    baseT=10
    annual['MinTemp(°C)']= min_temp(annual['Min Temp (°C)'])
    annual['GDD'] = ((annual['Max Temp (°C)'] + annual['MinTemp(°C)'])/2) -10
    annual['GDD'] = sure_Data(annual['GDD'])
    return annual



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
    run()
