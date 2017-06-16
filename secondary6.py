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

# define GDD_plot_byCity function to plot the GDD for the given city 
def GDD_plot_byCity(cityName,start=2013,end=2017):
	GDDfilename = filepath+'GDD_Value_'+cityName+'_'+str(start)+'_'+str(end)+'.csv'
	list_years = list(range(int(start),int(end)))
	GDD_mean = []
	fig = plt.figure(figsize=(12, 6))
	plt.title('GDD from '+str(start)+' to '+str(end)+', in '+ cityName)
	plt.ylabel('GDD in different years')
	plt.xlabel('Day of Year')
	plt.ylim(0,1000)
	plt.xlim(int(start)-1,int(end))
	Data = pd.read_csv(GDDfilename, encoding = 'utf-8',index_col=0)
	
	for year in list_years:
		instance = Data[Data['Date/Time'].str.contains(str(year))]
		GDD_mean.append(np.mean(instance['accGDD']))
	(m,b) = np.polyfit(list_years,GDD_mean,1)
	yp = np.polyval([m,b],list_years)			
	plt.scatter(list_years, GDD_mean,color= next(colors), label = "accGDD annual mean in "+cityName)
	plt.plot(list_years,yp)
	plt.legend(loc='upper left')	
	fig.savefig(plotpath+cityName+'/GDD_LinearRegression_'+cityName+'.png')

#obtain the data and calculate accumulate GDD
def parseData(data,infor):
	cityName = infor[0]
	start = infor[1]
	end = infor[2]
	list_years = list(range(int(start),int(end)+1))
	GDD_plot_byCity(cityName,start,end)   	

def run():
	files = get_allfiles()
	for element in files:
		Data = pd.read_csv(filepath+element, encoding = 'utf-8', index_col=0)
		placeInfo = element[:-4].split('_')[2:]
		parseData(Data,placeInfo)
    
if __name__ == '__main__':
    run()

