import wget
import numpy as np
import pandas as pd
import time as time
import math
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
# define the plot path
plotpath= (os.getcwd()+'/Plot/')

# choose different base temperature
T_baseList=[10,11,12,13,14,15]

# define the accumulated GDD function
def checkGDD(values):
    gdd = []
    item = 0
    for i in values:
        if i >= 0:
            item += i
        gdd.append(item)
    return gdd

# define the funtion to calculate GDD
def gdd_Tbase(i):
    CurrentPath = os.getcwd()
    filepath= (os.getcwd()+'/DataFiles/GDD_Data_HALIFAX_2013_2013.csv')
    annual = pd.read_csv(filepath, encoding = 'utf-8',index_col=0)
    a=annual['GDD']
    b=annual['GDD']
    annual['GDD'+str(i)]=(a+b)/2-T_baseList[i]
    annual['GDD'+str(i)]=checkGDD(annual['GDD'+str(i)])
    gddt=annual['GDD'+str(i)]
    #print(gddt)
    gddt=np.array(gddt)
    return gddt

def Main():
    color=iter(cm.rainbow(np.linspace(0,1,len(T_baseList))))
    # define the plot for different accumulated GDD 
    plt.subplot(1,1,1)
    for i in range(len(T_baseList)):
        c=next(color)
        plt.plot(gdd_Tbase(i),c=c,label ='T_base = '+str(T_baseList[i]))
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
    ax.set_ylabel('accumulated GDD on different T_bases', color='blue', fontsize=12)
    plt.title("Accumulated GDD of St.John's in 2013", color="blue", fontsize=14)
    plt.grid()
    plt.savefig("./Plot/differentTbase.png")
    
    
if __name__ == '__main__':
    Main()
