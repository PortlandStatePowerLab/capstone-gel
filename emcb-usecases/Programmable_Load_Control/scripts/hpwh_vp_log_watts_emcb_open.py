# Created by Midrar Adham
# Summer Term 2021
# midrar.adhm@gmail.com

####################################################
####################################################

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

# Plotting each EMCB case in a different function.

hpwh_log="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/hpwh_no_loadup_emcb_open.csv"
hpwh_vp="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/vp_data/hpwh_vp_no_load_up_emcb_open.csv"

#hpwh_vp="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/vp_data/hpwh_vp_no_load_up_emcb_open_version2.csv"


df1 = pd.read_csv(hpwh_log)
df2 = pd.read_csv(hpwh_vp)

# This function plots watts consumed from WH station vs watts consumed in VP website


def hpwh_vp_vs_log_no_loadup(log,vp):
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
    #ax[0].xaxis.set_major_locator(plt.NullLocator())
    ax[0].xaxis.set_major_locator(plt.MaxNLocator(30))
    #plt.xticks(rotation=90)
    ax[1].xaxis.set_major_locator(plt.MaxNLocator(30))
    ax[0].yaxis.set_major_locator(plt.MaxNLocator(10))
    ax[1].yaxis.set_major_locator(plt.MaxNLocator(10))
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
    ax[0].set_title('HPWH Consumed Watts: WH Station and VP')
    ax[0].annotate('VP Shed Command Received',xy=('06:45',0),xytext=('02:45',500),arrowprops=dict(arrowstyle='-|>'))
    ax[0].annotate('VP Shed Command Received',xy=('18:55',0),xytext=('13:55',500),arrowprops=dict(arrowstyle='-|>'))
    ax[0].annotate('VP Shed Command Received',xy=('19:55',0),xytext=('13:55',500),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received',xy=('06:45',0),xytext=('00:45',500),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received',xy=('18:55',0),xytext=('13:55',1000),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received',xy=('19:55',400),xytext=('13:55',1000),arrowprops=dict(arrowstyle='-|>'))
   


    #plt.show()
    #plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/hpwh/overleaf_figures/hpwh_vp_no_load_up_watts_emcb_open_original.png")
#hpwh_vp_vs_log_no_loadup(df1,df2)




hpwh_log="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/hpwh_emcb_open_load_up.csv"
hpwh_vp="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/vp_data/hpwh_load_up_emcbs_open.csv"

#hpwh_vp="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/vp_data/hpwh_vp_no_load_up_emcb_open_version2.csv"


df1 = pd.read_csv(hpwh_log)
df2 = pd.read_csv(hpwh_vp)

# This function plots watts consumed from WH station vs watts consumed in VP website

#ax[0] is vp file
#ax[1] is log file
def hpwh_vp_vs_log_loadup(log,vp):
    x = log['timestamp']
    x = pd.to_datetime(log['timestamp'])
    x = pd.to_datetime(x)
    x = x.dt.strftime('%H:%M')
    x2 = vp['time']
    x2 = pd.to_datetime(vp['time'])
    x2 = pd.to_datetime(x2)
    x2 = x2.dt.strftime('%H:%M')
    y = log['consumed_watts']
    y2 = vp['real-power']* 1000
    fig,ax = plt.subplots(2,figsize=(12,8))
    ax[0].xaxis.set_major_locator(plt.MaxNLocator(30))
    ax[1].xaxis.set_major_locator(plt.MaxNLocator(30))
    ax[0].yaxis.set_major_locator(plt.MaxNLocator(10))
    ax[1].yaxis.set_major_locator(plt.MaxNLocator(10))
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
    ax[0].set_title('HPWH Consumed Watts: WH Station and VP')
    

    ax[0].annotate('VP Shed Command Received',xy=('06:47',0),xytext=('02:27',1200),arrowprops=dict(arrowstyle='-|>'))
    ax[0].annotate('VP Shed Command Received',xy=('18:57',0),xytext=('15:47',500),arrowprops=dict(arrowstyle='-|>'))
    ax[0].annotate('VP Shed Command Received',xy=('20:02',0),xytext=('15:47',500),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received',xy=('06:41',0),xytext=('01:41',1200),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received',xy=('18:55',0),xytext=('13:55',1000),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received',xy=('19:56',400),xytext=('13:55',1000),arrowprops=dict(arrowstyle='-|>'))
   

    ax[0].annotate('Loadup Command Received',xy=('05:32',0),xytext=('00:47',600),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('Loadup Command Received',xy=('05:29',0),xytext=('00:47',600),arrowprops=dict(arrowstyle='-|>'))

    #plt.show()
    plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/hpwh/overleaf_figures/hpwh_vp_load_up_watts_emcb_open.png")
hpwh_vp_vs_log_loadup(df1,df2)
