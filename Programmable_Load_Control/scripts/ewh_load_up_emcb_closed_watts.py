import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

# Plotting each EMCB case in a different function.

ewh_log ="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/loadup_emcb_closed.csv"
ewh_vp="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/vp_data/ewh_vp_loadup_emcb_closed.csv"

df1 = pd.read_csv(ewh_log)
df2 = pd.read_csv(ewh_vp)

# This function plots watts consumed from WH station vs watts consumed in VP website


def ewh_vp_vs_log_loadup(log,vp):
    x = log['timestamp']
    x = pd.to_datetime(log['timestamp'])
    x = pd.to_datetime(x)
    x = x.dt.strftime('%H:%M')
    x2 = vp['time']
    x2 = pd.to_datetime(vp['time'])
    x2 = pd.to_datetime(x2)
    x2 = x2.dt.strftime('%H:%M')
    y = log['consumed_watts']
    y2 = vp['circuit-breaker-total-power']* 1000
    fig,ax = plt.subplots(2,figsize=(12,8))
    ax[0].xaxis.set_major_locator(plt.NullLocator())
    ax[1].xaxis.set_major_locator(plt.MaxNLocator(30))
    ax[0].plot(x2,y2,label='VP Recorded Data')
    ax[1].plot(x,y,label='WH Station Data')
    ax[1].set_xlabel('time (Hours:minutes)')
    ax[0].set_ylabel('Real Power (W)')
    ax[1].set_ylabel('Real Power (W)')
    plt.xticks(rotation=90)
    x2_max = vp['time'].max()
    ax[0].set_xlim([0,x2_max])
    x_max = log['timestamp'].max()
    ax[1].set_xlim([0,x_max]) 
    ax[0].legend(loc='upper right')
    ax[1].legend(loc='upper right')
    ax[0].set_title('EWH Consumed Watts: WH Station and VP')
    ax[0].annotate('Load Up Command Received',xy=('06:30',0),xytext=(0,200),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('Load Up Command Received',xy=('06:30',0),xytext=(0,200),arrowprops=dict(arrowstyle='-|>'))
    ax[0].annotate('Load Up Command Received',xy=('18:45',0),xytext=(150,700),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('Load Up Command Received',xy=('18:44',0),xytext=(700,700),arrowprops=dict(arrowstyle='-|>'))

    #plt.show()
    #plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/ewh/overleaf_figures/ewh_load_up_emcb_closed.png")
#ewh_vp_vs_log_loadup(df1,df2)



####################################
# Plotting No Load Up EMCB Closed
####################################



ewh_log ="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/Noloadup_emcb_closed.csv"
ewh_vp="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/vp_data/ewh_vp_Noloadup_emcb_closed.csv"

df1 = pd.read_csv(ewh_log)
df2 = pd.read_csv(ewh_vp)

# This function plots watts consumed from WH station vs watts consumed in VP website


def ewh_vp_vs_log_No_loadup(log,vp):
    x = log['timestamp']
    x = pd.to_datetime(log['timestamp'])
    x = pd.to_datetime(x)
    x = x.dt.strftime('%H:%M')
    x2 = vp['time']
    x2 = pd.to_datetime(vp['time'])
    x2 = pd.to_datetime(x2)
    x2 = x2.dt.strftime('%H:%M')
    y = log['consumed_watts']
    y2 = vp['circuit-breaker-total-power']* 1000
    fig,ax = plt.subplots(2,figsize=(12,8))
    ax[0].yaxis.set_major_locator(plt.MaxNLocator(6))
    ax[1].yaxis.set_major_locator(plt.MaxNLocator(6))
    ax[0].xaxis.set_major_locator(plt.MaxNLocator(30))
    ax[1].xaxis.set_major_locator(plt.MaxNLocator(30))
    ax[0].plot(x2,y2,label='VP Recorded Data')
    ax[1].plot(x,y,label='WH Station Data')
    ax[1].set_xlabel('time (Hours:minutes)')
    ax[0].set_ylabel('Real Power (W)')
    ax[1].set_ylabel('Real Power (W)')
    ax[0].tick_params(axis='x',rotation=90)
    ax[1].tick_params(axis='x',rotation=90)
    x2_max = vp['time'].max()
    ax[0].set_xlim([0,x2_max])
    x_max = log['timestamp'].max()
    ax[1].set_xlim([0,x_max]) 
    ax[0].legend(loc='upper right')
    ax[1].legend(loc='upper right')
    ax[0].set_title('EWH Consumed Watts: WH Station and VP')
    #plt.show()
    plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/ewh/overleaf_figures/ewh_No_load_up_emcb_closed.png")
ewh_vp_vs_log_No_loadup(df1,df2)


