import numpy as np
import pandas as pd
import os

# Read the data from a csv file by given file path.
def extract_data_from_csv(FilePath):
    try:
        File_Data = pd.read_csv(FilePath, encoding = 'utf-8', delimiter = ',' ,skiprows=0)
    except Exception as e:
        print("Error in Reading", FilePath)
        print(e)
    Data = pd.DataFrame(File_Data)
    Data.replace('', np.nan, inplace = True)
    Data = Data.dropna()
    Index = Data.keys()
    Date, maxTemp, minTemp = np.array(Data[Index[1]]),np.array(Data[Index[2]]), np.array(Data[Index[3]])
    
    return Data, Date, maxTemp, minTemp



 
