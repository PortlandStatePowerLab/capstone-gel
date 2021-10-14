import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

ewh_log ="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/loadup_emcb_closed.csv"

df1 = pd.read_csv(ewh_log)

# This function plots energyTake closed emcb for hpwh


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
    ax.annotate('Load Up Command Received',xy=('06:31',675),xytext=(80,800),arrowprops=dict(arrowstyle='-|>'))
    ax.annotate('Load Up Command Received',xy=('18:43',825),xytext=(680,1000),arrowprops=dict(arrowstyle='-|>'))

    #plt.show()
    #plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/ewh/overleaf_figures/ewh_load_up_energyTake_emcb_closed.png")
#ewh_energyTake_loadup(df1)



####################################
ewh_log ="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/Noloadup_emcb_closed.csv"

df1 = pd.read_csv(ewh_log)

# This function plots energyTake closed emcb for hpwh


def ewh_energyTake_No_loadup(log):
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
    #plt.show()
    plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/ewh/overleaf_figures/ewh_No_load_up_energyTake_emcb_closed.png")
ewh_energyTake_No_loadup(df1)


