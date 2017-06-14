#!/usr/bin/Python
import os, sys, stat
import pandas as pd
import numpy as np
import getopt
import shutil
import matplotlib.pyplot as plt
import itertools


# define the roots
plotpath= (os.getcwd()+'/Plot/')
filepath= (os.getcwd()+'/DataFiles/')

colors = itertools.cycle(['b','g','r','c','m','y','k'])

# get the files
def get_allfiles():
	files = os.listdir(filepath)
	files = [file for file in files if file.startswith('GDD')]
	return files

# define AccGDD_plot_byCity function to plot the accumulated GDD for the given cities
def AccGDD_plot_byCity(cityName,start,end,data):
	if not os.path.exists(plotpath+str(cityName)):
		os.makedirs(plotpath+str(cityName))
	fig = plt.figure(figsize=(12, 6))
	plt.title('Accumulated GDD in '+str(cityName)+' from '+str(start)+' to '+str(end))
	plt.ylabel('Accumulated GDD')
	plt.xlabel('Day of Year')
	list_years = list(range(int(start),int(end)+1))
	for year in list_years:
		annual = data[data['Date/Time'].str.contains(str(year))] 
		plt.plot(annual.index.values.tolist(), annual['accGDD'],color=next(colors), label = "Accumulated GDD in "+str(year))
		plt.legend(loc='upper left')
	fig.savefig(plotpath+str(cityName)+'/accGDD_'+str(start)+'_'+str(end)+'.png')

# define AccGDD_plot_byYear function to plot the accumulated GDD for the given Years 
def AccGDD_plot_byYear(files,start=2013,end=2017):
	list_years = list(range(int(start),int(end)+1))
	for year in list_years:
		fig = plt.figure(figsize=(12, 6))
		plt.title('Accumulated GDD in '+str(year)+' among '+str(len(files))+' cities')
		plt.ylabel('Accumulated GDD')
		plt.xlabel('Day of Year')
		for element in files:
			placeInfo = element[:-4].split('_')[2:]
			Data = pd.read_csv(filepath+element, encoding = 'utf-8',index_col=0)
			instance = Data[Data['Date/Time'].str.contains(str(year))]			
			plt.plot(instance.index.values.tolist(), instance['accGDD'],color=next(colors), label = "Accumulated GDD in "+str(placeInfo[0]))
			plt.legend(loc='upper left')
		fig.savefig(plotpath+'accGDD_'+str(year)+'.png')

# define parseData function that read all data from files
def parseData(data,infor):
	cityName = infor[0]
	start = infor[1]
	end = infor[2]
	AccGDD_plot_byCity(cityName,start,end,data)
	

# define run function which insider of main function
def run():
	files = get_allfiles()
	for element in files:
		Data = pd.read_csv(filepath+element, encoding = 'utf-8',index_col=0)
		placeInfo = element[:-4].split('_')[2:] # city startyear endyear
		parseData(Data,placeInfo)

	AccGDD_plot_byYear(files,placeInfo[1],placeInfo[2])


# define the main function
if __name__ == '__main__':
	run()

