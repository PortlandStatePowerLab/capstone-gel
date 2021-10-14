import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

hpwh_log ="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/hpwh_loadup_emcb_closed.csv"

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
    ax.annotate('Load Up Command Received',xy=('05:54',450),xytext=(12,15),arrowprops=dict(arrowstyle='-|>'))
    #plt.show()
    plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/hpwh/overleaf_figures/hpwh_load_up_energyTake_emcb_closed.png")
#hpwh_energyTake_loadup(df1)



####################################
# Plotting EnergyTake No Load Up EMCB Closed
####################################

hpwh_log ="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/Noloadup_emcb_closed.csv"

df1 = pd.read_csv(hpwh_log)

# This function plots energyTake closed emcb for hpwh No Load Up


def hpwh_energyTake_No_loadup(log):
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
    plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/hpwh/overleaf_figures/hpwh_No_load_up_energyTake_emcb_closed.png")
hpwh_energyTake_No_loadup(df1)
