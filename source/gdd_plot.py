import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
from extract_data_from_csv import extract_data_from_csv

# Plotting GDD for a given city
def gdd_plot(gdd, cityName, gColor):
    plt.subplot(1,1,1)
    X = np.linspace(1, 12, 365, endpoint=True)
    plt.plot(X, gdd, color=gColor, label = cityName)
    plt.legend(loc='upper left')
    ax = plt.gca() 
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(8)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

    ax.set_xlabel('Months', color='black', fontsize=14)
    ax.set_ylabel('Cumulative GDD (>10°C)', color='black', fontsize=14)
    plt.title('Accumulated Growing Degree Days', color="black", fontsize=14)
    return plt
    
def Main():
    # Taking the arguments from command line. 
    parser = argparse.ArgumentParser()
    parser.add_argument("-st", dest="stationId", nargs = '*', help="Please provide a list of station Id.")
    parser.add_argument("-ct", dest="cityName", nargs = '*', help="Please provide a list of city names corresponding to stations.")
    parser.add_argument("-gc", dest="gColor", nargs = '*', help="Please provide the colors for each city graph.")
	
    args = parser.parse_args()
	
    cityData = []
    for i in range(len(args.stationId)):
    	# Reading the data from downloaded .csv files. 
        CurrentPath = os.getcwd()
        FilePath= (CurrentPath+'/DataFiles/GDD_Data_'+args.cityName[i]+'.csv')
        Data, Date, maxTemp, minTemp = extract_data_from_csv(FilePath)
        cityData.append(Data['GDD'])
    
    for i in range(len(cityData)):
        gdd_plt = gdd_plot(cityData[i], args.cityName[i], args.gColor[i])
		
    gdd_plt.savefig("./Plots/GDD_Plot.png")

if __name__ == '__main__':
    Main()
