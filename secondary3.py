import wget
import numpy as np
import pandas as pd
import time as time
import math
import os
import csv
import matplotlib.pyplot as plt
import itertools

colors = itertools.cycle(['b','g','r','c','m','y','k'])


plotpath = (os.getcwd()+'/Plot/')
filepath = (os.getcwd()+'/DataFiles/')

# choose different base temperature
T_baseList=[5,10,15]

# get the files
def get_allfiles():
	files = os.listdir(filepath)
	files = [file for file in files if file.startswith('GDD')]
	return files

#calculating the values of GDD
def calculate_GDD(annual,baseT=T_baseList):
	for value in T_baseList:
		if value != 10:
			annual['Min Temp (°C)']= [x if x > value else value for x in annual['Min Temp (°C)']] 
			annual['rGDD'] = ((annual['Max Temp (°C)'] + annual['Min Temp (°C)'])/2) -value
			annual['GDD_'+str(value)] = [x if x>0 else 0 for x in annual['rGDD']]
			annual['accGDD'+str(value)]=np.cumsum(annual['GDD_'+str(value)])
			del annual['rGDD']
	return annual


# define AccGDD_plot_byTbase function to plot the accumulated GDD for the given Tbase 
def AccGDD_plot_byTbase(cityName,start=2013,end=2017,baseT=T_baseList):
	GDDfilename = filepath+'GDD_Value_'+cityName+'_'+str(start)+'_'+str(end)+'.csv'
	list_years = list(range(int(start),int(end)+1))
	Data = pd.read_csv(GDDfilename, encoding = 'utf-8',index_col=0)
	for year in list_years:
		fig = plt.figure(figsize=(12, 6))
		plt.title('Different Base Accumulated GDD in '+str(year)+', '+ cityName)
		plt.ylabel('Different Base Accumulated GDD')
		plt.xlabel('Day of Year')
		instance = Data[Data['Date/Time'].str.contains(str(year))]			
		plt.plot(instance.index.values.tolist(), instance['accGDD'],color=next(colors), label = "10 Base Accumulated GDD ")
		for base in T_baseList:
			if base != 10:
				plt.plot(instance.index.values.tolist(), instance['accGDD'+str(base)],color=next(colors), label = str(base)+" Base Accumulated GDD ")
		plt.legend(loc='upper left')
		fig.savefig(plotpath+cityName+'/accGDD_Base_'+str(year)+'.png')

#obtain the data and calculate accumulate GDD
def parseData(data,infor):
	cityName = infor[0]
	start = infor[1]
	end = infor[2]
	list_years = list(range(int(start),int(end)+1))

	GDDfilename = filepath+'GDD_Value_'+cityName+'_'+start+'_'+end+'.csv'
	global T_baseList
	DataBuffer = []
	for year in list_years:
		annual = data[data['Date/Time'].str.contains(str(year))]
		df=calculate_GDD(annual)
		DataBuffer.append(df)
	with open(GDDfilename, 'w+') as datafile:
		Data = pd.concat(DataBuffer) 
		Data.to_csv(GDDfilename, sep=',', encoding='utf-8')
	AccGDD_plot_byTbase(cityName,start=2013,end=2017,baseT=T_baseList)   	

def run():
	files = get_allfiles()
	for element in files:
		Data = pd.read_csv(filepath+element, encoding = 'utf-8', index_col=0)
		placeInfo = element[:-4].split('_')[2:]
		parseData(Data,placeInfo)
    
if __name__ == '__main__':
    run()

