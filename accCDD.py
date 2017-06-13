import os
import re
import pandas as pd
import matplotlib.pyplot as plt

dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')

if not os.path.exists(os.path.join(os.getcwd(),'ProcessData')):
    os.makedirs(os.path.join(os.getcwd(),'ProcessData'))

filepath = os.path.join(os.getcwd(),'DataFiles')

files = os.listdir(filepath)

files = [file for file in files if file.startswith('GDD')]

types = ['r-','b-','g-','y-']

for file,type in zip(files,types[:len(files)]):
    
    m = re.match('GDD_Data_([ \w]+)_\d+_\d+',file)
    city = m.group(1)
   
    
    temp = pd.read_csv(os.path.join(filepath,file),sep=',',parse_dates=['Date/Time'], date_parser=dateparse)
    temp.columns=['Index','Date','MaxTemp','MinTemp']
    temp['MinTemp'] = [x if x > 10 else 10 for x in temp['MinTemp']]
    temp['rGDD'] = (temp['MaxTemp']+temp['MinTemp'])/2.0 - 10.0
    temp['GDD'] = [x if x>0 else 0 for x in temp['rGDD']]
    temp = temp.sort_values(['Date'])
    temp['accGDD'] = temp['GDD'].cumsum()
    temp.to_csv(os.path.join(os.getcwd(),'ProcessData',city+'.csv'),index=False)

    plt.plot(temp['Date'],temp['accGDD'],type,label= city)
    

plt.legend(loc='upper left')
plt.show()
