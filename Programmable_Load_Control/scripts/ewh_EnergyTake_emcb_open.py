import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

# Plotting each EMCB case in a different function.

ewh_log='/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/ewh_no_load_up_emcb_open_aug17_18.csv'


df1 = pd.read_csv(ewh_log)

# This function plots watts consumed from WH station vs watts consumed in VP website


def ewh_energyTake_no_loadup(log):
    x = log['timestamp']
    x = pd.to_datetime(log['timestamp'])
    x = pd.to_datetime(x)
    x = x.dt.strftime('%d %H:%M')
    y = log['real_available_watts']
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    ax.xaxis.set_major_locator(plt.MaxNLocator(40))
    ax.plot(x,y,label='WH Station Data')
    ax.set_xlabel('time (Day Hours:minutes)')
    ax.set_ylabel('EnergyTake (Wh)')
    plt.xticks(rotation=90)
    x_max = log['timestamp'].max()
    ax.set_xlim([0,x_max]) 
    ax.set_title('EnergyTake VS Time')
    ax.legend(loc='upper right')
    ax.annotate('VP Shed Command Received',xy=('17 06:45',0),xytext=('17 00:00',-100),arrowprops=dict(arrowstyle='-|>'))
    ax.annotate('VP Shed Command Received (NR)',xy=('17 18:55',0),xytext=('17 08:20',100),arrowprops=dict(arrowstyle='-|>'))
    ax.annotate('VP Shed Command Received (NR)',xy=('17 19:55',0),xytext=('17 08:20',100),arrowprops=dict(arrowstyle='-|>'))
    ax.annotate('VP Shed Command Received',xy=('18 06:41',0),xytext=('17 22:55',-100),arrowprops=dict(arrowstyle='-|>'))
    ax.annotate('VP Shed Command Received',xy=('18 18:56',0),xytext=('18 09:00',250),arrowprops=dict(arrowstyle='-|>'))
    ax.annotate('VP Shed Command Received (NR)',xy=('18 19:55',0),xytext=('18 12:00',-100),arrowprops=dict(arrowstyle='-|>'))
    #plt.show()
    #plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/ewh/overleaf_figures/ewh_EnergyTake_no_load_up_watts_emcb_open.png")

#ewh_energyTake_no_loadup(df1)




ewh_log='/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/ewh_emcb_open_load_up.csv'


df1 = pd.read_csv(ewh_log)

# This function plots watts consumed from WH station vs watts consumed in VP website


def ewh_energyTake_loadup(log):
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
    ax.annotate('VP Shed Command Received',xy=('06:39',75),xytext=('07:23',-100),arrowprops=dict(arrowstyle='-|>'))
    ax.annotate('VP Shed Command Received',xy=('18:55',150),xytext=('14:48',-100),arrowprops=dict(arrowstyle='-|>'))
    ax.annotate('VP Shed Command Received',xy=('19:56',75),xytext=('14:48',-100),arrowprops=dict(arrowstyle='-|>'))

    ax.annotate('Loadup Command Received',xy=('06:16',750),xytext=('00:40',1000),arrowprops=dict(arrowstyle='-|>'))
    ax.annotate('Loadup Command Received',xy=('18:16',825),xytext=('14:00',1000),arrowprops=dict(arrowstyle='-|>'))


    #plt.show()
    plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/ewh/overleaf_figures/ewh_EnergyTake_load_up_emcb_open.png")

ewh_energyTake_loadup(df1)
