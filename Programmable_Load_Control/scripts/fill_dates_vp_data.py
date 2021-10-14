# Author Midrar Adham
# Date: Aug-20-2021

import pandas as pd
from datetime import datetime as dt

path="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/vp_data/ewh_no_load_up_emcb_open_aug_17_18.csv"
df = pd.read_csv(path)

destination='/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/vp_data/ewh_load_up_emcb_open_aug_17_19_resampled.csv'

def resampling_timestamp(path,destination):
    clean = df.set_index('time')                        # Set index column to be the time column
    dup = clean[clean.index.duplicated()].index         # Get the duplicate rows 
    clean = clean.drop(dup)                             # Drop duplicate rows
    head =clean.head(1).index                           # Get the first row
    tail =clean.tail(1).index                           # Get the last row


    clean.index=clean.index.astype('datetime64[ns]')    # Convert time type to datetime
    clean = clean.resample('5Min').sum()               # Put zeroes in the other column values
    #clean = clean.resample('1Min').fillna(0)           # fill values before 


# The following line resamples the timestamp to one minute and fill in the missing values with zeroes
    #clean = clean.resample('1Min').asfreq(fill_value=0)
    clean.to_csv(destination)                             # Write to csv file
    print(clean)
resampling_timestamp(path,destination)
