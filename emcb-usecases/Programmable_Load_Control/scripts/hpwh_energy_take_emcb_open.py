# Created by Midrar Adham
# Summer Term 2021
# midrar.adhm@gmail.com

####################################################
####################################################

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

#hpwh_log="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/hpwh_no_loadup_emcb_open.csv"

hpwh_log="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/hpwh_emcb_open_no_load_up_v2.csv"


df1 = pd.read_csv(hpwh_log)

# This function plots energyTake closed emcb for hpwh


def hpwh_energyTake_no_loadup(log):
    x = log['timestamp']
    x = pd.to_datetime(log['timestamp'])
    x = pd.to_datetime(x)
    x = x.dt.strftime('%H:%M')
    y = log['real_available_Wh']
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    ax.xaxis.set_major_locator(plt.MaxNLocator(40))
    ax.plot(x,y,label='WH Station Data')
    ax.set_xlabel('time (Hours:minutes)')
    ax.set_ylabel('EnergyTake (Wh)')
    plt.xticks(rotation=90)
    x_max = log['timestamp'].max()
    ax.set_xlim([0,x_max]) 
    ax.set_title('EnergyTake VS Time')
    ax.legend(loc='upper right')
    ax.annotate('VP Shed Command Received',xy=('06:41',625),xytext=('00:50',100),arrowprops=dict(arrowstyle='-|>'))
    ax.annotate('VP Shed Command Received',xy=('18:55',150),xytext=('14:07',300),arrowprops=dict(arrowstyle='-|>'))
    ax.annotate('VP Shed Command Received',xy=('19:56',1275),xytext=('14:07',300),arrowprops=dict(arrowstyle='-|>'))
    #plt.show()
    plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/hpwh/overleaf_figures/hpwh_no_load_up_energyTake_emcb_open.png")
hpwh_energyTake_no_loadup(df1)



hpwh_log="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/hpwh_emcb_open_load_up.csv"

df1 = pd.read_csv(hpwh_log)

# This function plots energyTake closed emcb for hpwh


def hpwh_energyTake_loadup(log):
    x = log['timestamp']
    x = pd.to_datetime(log['timestamp'])
    x = pd.to_datetime(x)
    x = x.dt.strftime('%H:%M')
    y = log['real_available_Wh']
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    ax.xaxis.set_major_locator(plt.MaxNLocator(40))
    ax.plot(x,y,label='WH Station Data')
    ax.set_xlabel('time (Hours:minutes)')
    ax.set_ylabel('EnergyTake (Wh)')
    plt.xticks(rotation=90)
    x_max = log['timestamp'].max()
    ax.set_xlim([0,x_max]) 
    ax.set_title('EnergyTake VS Time')
    ax.legend(loc='upper right')
    ax.annotate('Loadup Command Received',xy=('05:31',525),xytext=('00:41',700),arrowprops=dict(arrowstyle='-|>'))

    ax.annotate('VP Shed Command Received',xy=('06:41',0),xytext=('02:01',-100),arrowprops=dict(arrowstyle='-|>'))
    ax.annotate('VP Shed Command Received',xy=('18:55',150),xytext=('14:07',-100),arrowprops=dict(arrowstyle='-|>'))
    ax.annotate('VP Shed Command Received',xy=('19:56',1275),xytext=('14:07',1275),arrowprops=dict(arrowstyle='-|>'))

    #plt.show()
    #plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/hpwh/overleaf_figures/hpwh_load_up_energyTake_emcb_open.png")
#hpwh_energyTake_loadup(df1)

