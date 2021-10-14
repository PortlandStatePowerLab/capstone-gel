# I'm trying to calculate temperature from Water Heaters EnergyTake. Let's see how it goes ..
# Created by Midrar Adham
# Summer Term 2021
# midrar.adhm@gmail.com

####################################################
####################################################


import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

cols = ['timestamp','idk1','idk2','idk3','idk4','element_rated_watts','available_energy','rated_available_energy','real_watts','op_state']
hpwh_path = "/Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/log_files/ewh/csv_logs/DER_Data_2021-07-29.csv"

def temp_calc(hpwh,cols):
    df = pd.read_csv(hpwh_path,names=cols)
    energy = df['available_energy']
    energy_pct = energy/3630                    # 3630 is the total watts-hour available when tank temp is zero. Leighton's Thesis
    temp_pct = energy_pct * 120                 # Multiply the energy percent by the tank's setpoint
    curr_temp = 120 - temp_pct                  # Get the current tank's temp based on the current available energy.
    df['water_temp'] = curr_temp              # Append curr_temp in a new column of the dataframe
    return df



def plot(df):
    x1 = pd.to_datetime(df['timestamp'])
    x1 = pd.to_datetime(x1)
    x1 = x1.dt.strftime('%H:%M')
    y1 = df['available_energy']
    y2 = df['water_temp']
    print(y2)
    fig = plt.figure(figsize=(12,4))
    ax1 = fig.add_subplot(111)
    ax1.xaxis.set_major_locator(plt.MaxNLocator(60))
    plt.xticks(rotation=45)
    ax1.yaxis.tick_left()
    ax1.set_ylabel("EnergyTake (Wh)")
    ax2 = ax1.twinx()
    ax1.plot(x1,y1)
    ax2.plot(x1,y2,color='red')
    ax2.patch.set_alpha(0.5)
    ax2.xaxis.set_major_locator(plt.MaxNLocator(60))
    ax2.yaxis.tick_right()
    ax2.set_ylabel('Water_Temp in F')
    plt.show()

temp_calc(hpwh_path,cols)
temp_df = temp_calc(hpwh_path,cols)

plot(temp_df)
