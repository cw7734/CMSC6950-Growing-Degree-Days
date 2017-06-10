from bokeh.charts import Donut, show, output_file
from bokeh.charts.utils import df_from_json
from bokeh.sampledata.olympics2014 import data
from bokeh.charts import Bar, output_file, show, save
import csv
import os
import numpy as np
import pandas as pd
import argparse
from extract_data_from_csv import extract_data_from_csv

## Reference
## http://store.msuextension.org/publications/AgandNaturalResources/MT200103AG.pdf
## GDD For BARLEY,
## The GDD of BARLEY 'Emergence':109-145,'Leaf_development':146-184,'Tillering':185-360,'Stem_elongation':489-555

def getGroup(GDD):
    group = []
    for i in GDD:
        if( i >= 109 and i <= 145):
            group.append('Emergence')
        elif ( i >= 146 and i <= 184):
            group.append('Leaf_development')
        elif ( i >= 185 and i <= 360):
            group.append('Tillering')
        elif ( i >= 361 and i <= 555):
            group.append('Stem_elongation')
        elif ( i >= 556 and i <= 936):
            group.append('Anthesis')
        elif ( i >= 937 and i <= 1145):
            group.append('Seed_fill')
        elif ( i >= 1146 and i <= 1438):
            group.append('Dough_stage')
        elif ( i >= 1439 and i <= 1522):
            group.append('Maturity_complete')
        else:
            group.append('No Growth')

    return group

def Main():
    # Taking the arguments from command line. 
    parser = argparse.ArgumentParser()
    parser.add_argument("-st", dest="stationId", nargs = '*', help="Please provide a list of station Id.")
    parser.add_argument("-ct", dest="cityName", nargs = '*', help="Please provide a list of city names corresponding to stations.")
    
    args = parser.parse_args()
	
    CurrentPath = os.getcwd()
	
    for i in range(len(args.stationId)):
        FilePath= (CurrentPath+'/DataFiles/GDD_Data_'+args.cityName[i]+'.csv')
        Data, Date, MaxTemp, MinTemp = extract_data_from_csv(FilePath)
        Index = Data.keys()
        Data['group'] = getGroup(Data[Index[4]])
        Data['month'] = pd.DatetimeIndex(Date).month

        plot = Bar(Data,label='month', values='GDD',agg='median', group='group',
        title="GDD of Barley In Bar Chart for "+args.cityName[i], legend='top_left')
        output_file("./Plots/FinalTask_"+args.cityName[i]+".html", title="Final Task for ("+args.cityName[i]+")")
        save(plot)

if __name__ == '__main__':
    Main()
