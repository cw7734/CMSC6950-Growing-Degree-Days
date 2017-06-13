#!/usr/bin/Python
import os, sys, stat
import pandas as pd
import numpy as np
import getopt
import shutil
import matplotlib.pyplot as plt

# define the roots
plotpath= (os.getcwd()+'/Plot/')
filepath1= (os.getcwd()+'/DataFiles/GDD_Data_HALIFAX_2013_2013.csv')
filepath2= (os.getcwd()+'/DataFiles/GDD_Data_ST JOHNS_2013_2013.csv')
filepath3= (os.getcwd()+'/DataFiles/GDD_Data_TORONTO_2013_2013.csv')
filepath4= (os.getcwd()+'/DataFiles/GDD_Data_VANCOUVER_2013_2013.csv')


def run():
    fig = plt.figure(figsize=(12, 6))
    plt.title('Accumulated GDD for given cities in 2013 ')
    plt.ylabel('Accumulated GDD')
    plt.xlabel('Day of Year')
    annual1 = pd.read_csv(filepath1, encoding = 'utf-8',index_col=0)
    annual2 = pd.read_csv(filepath2, encoding = 'utf-8',index_col=0)
    annual3 = pd.read_csv(filepath3, encoding = 'utf-8',index_col=0)
    annual4 = pd.read_csv(filepath4, encoding = 'utf-8',index_col=0)
    plt.plot(annual1['accGDD'], marker=',',color="red", label = "Halifax")
    plt.plot(annual2['accGDD'], marker=',',color="blue", label = "St.John's")
    plt.plot(annual3['accGDD'], marker=',',color="green", label = "Toronto")
    plt.plot(annual4['accGDD'], marker=',',color="black", label = "Vancouver")
    plt.legend(loc='upper left')
    plt.grid()
    fig.savefig('Plot/accGdd'+'.png')

	


                
      
# define the main function
if __name__ == '__main__':
	run()

