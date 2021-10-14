# This script plot two x axis and two y axis in the same plot. This is used to verify the recorded data from the power analyzer and the recorded data from virtualPeaker.com are the same.

import pandas as pd
import matplotlib.pyplot as plt
import datetime
from matplotlib import dates as md
import matplotlib.dates as mdates
import numpy as np
#####################################################
#####################################################
#####################################################

df = pd.read_csv('/Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/ewh_hpwh/Day1_Data/updated_data_day2.csv',parse_dates=True)


df2 = pd.read_csv('/Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/ewh_hpwh/Day1_Data/data.csv',parse_dates=True)


print(df[df['watts_Sum_EWH']> 100])

# convert df timestamp object to datetime

df['timestamp'] = pd.to_datetime(df['timestamp'])

# Change the format from YYYY-MM-DD HH:MM:SS to HH:MM

df['timestamp'] = df['timestamp'].dt.strftime('%H:%M')

# convert df timestamp object to datetime

df2['time'] = pd.to_datetime(df2['time'])

# Change the format from YYYY-MM-DD HH:MM:SS to HH:MM

df2['time'] = df2['time'].dt.strftime('%H:%M')


fig = plt.figure()
ax = fig.add_subplot(111, label="1")
ax2 = fig.add_subplot(111,label="2",frame_on=False)
# ax3 = fig.add_subplot(111,label="3",frame_on=False)

ax.plot(df['timestamp'],df['watts_Sum_HPWH'],color='r')
ax.set_xlabel("timestamp_PA",color='r')
ax.set_ylabel("real Power (W)",color='r')
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
ax.tick_params(axis='x',color='r')
ax.tick_params(axis='y',color='r')
ax.xaxis.set_major_locator(plt.MaxNLocator(9))
ax2.xaxis.set_major_locator(plt.MaxNLocator(9))
ax2.plot(df2['time'],df2['real-power'],color='b')
ax2.xaxis.tick_top()
ax2.yaxis.tick_right()
ax2.set_xlabel('timestamp_VP',color='b')
ax2.set_ylabel('Real Power (kW)',color='b')
ax2.xaxis.set_label_position('top') 
ax2.yaxis.set_label_position('right') 
ax2.tick_params(axis='x', colors="b")
ax2.tick_params(axis='y', colors="b")
plt.show()

