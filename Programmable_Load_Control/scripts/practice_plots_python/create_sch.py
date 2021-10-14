


from termcolor import colored
import pandas as pd
from itertools import cycle
import os
import numpy as np
print(colored('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------','cyan'))

print(colored('This script creates a water demand profile for water heater in GLD. I cheated here by copying a timestamp column from existing glm output file and pasted in the new csv file\n','yellow'))

print(colored('First of all, I created a list of zeroes as shown in line 14 and put it in a dataframe. Then I wrote both columns to the new csv file. in line 17, I switched the order of the columns. Otherwise, GLD will not be able to read the csv file.','yellow'))

print(colored('The old csv file will be commented out but it is a trick if you find creating timestamp in python tiresome','yellow'))

print(colored('So you need to run Controlled_WH_4.glm file before running this script','yellow'))

print(colored('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------','cyan'))

print(colored('understand the instructions? (yes/no)','red'))
user = input()
if user == 'yes':
    print(colored('Good luck!','yellow'))
    pass
else:
    print(colored('Read it again and then run the script!','yellow'))
    print(colored('Need help? contact midrar.adhm@gmail.com','yellow'))
    quit()

df = pd.read_csv('../GLD_model/wh_1.csv',skiprows=8)
df['# timestamp'] = df['# timestamp'].str.replace('UTC','')

df2 = pd.DataFrame(0,index=np.arange(len(df['# timestamp'])),columns=['water_demand'])

df2['# timestamp'] = df['# timestamp'].copy()
df2 = df2[['# timestamp','water_demand']]
df2.to_csv('../GLD_model/water_demand.csv',index=False)
