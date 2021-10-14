import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

# Plotting each EMCB case in a different function.

ewh_log='/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/ewh_no_load_up_emcb_open_aug17_18.csv'
ewh_vp='/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/vp_data/ewh_no_load_up_emcb_open_aug_17_18_resampled.csv'


df1 = pd.read_csv(ewh_log)
df2 = pd.read_csv(ewh_vp)

# This function plots watts consumed from WH station vs watts consumed in VP website


def ewh_vp_vs_log_no_loadup(log,vp):
    x = log['timestamp']
    x = pd.to_datetime(log['timestamp'])
    x = pd.to_datetime(x)
    x = x.dt.strftime('%d %H:%M')
    x2 = vp['time']
    x2 = pd.to_datetime(vp['time'])
    x2 = pd.to_datetime(x2)
    x2 = x2.dt.strftime('%d %H:%M')
    y = log['consumed_watts']
    y2 = vp['real-power']* 1000
    fig,ax = plt.subplots(2,figsize=(12,8))
    ax[0].xaxis.set_major_locator(plt.MaxNLocator(30))
    ax[1].xaxis.set_major_locator(plt.MaxNLocator(30))
    ax[0].yaxis.set_major_locator(plt.MaxNLocator(10))
    ax[1].yaxis.set_major_locator(plt.MaxNLocator(10))
    ax[0].plot(x2,y2,label='VP Recorded Data')
    ax[1].plot(x,y,label='WH Station Data')
    ax[1].set_xlabel('timestamp (Day Hours:Minutes)')
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
    ax[0].annotate('VP Shed Command Received',xy=('17 06:45',0),xytext=('17 02:45',500),arrowprops=dict(arrowstyle='-|>'))
    ax[0].annotate('VP Shed Command Received (NR)',xy=('17 18:55',0),xytext=('17 13:55',1000),arrowprops=dict(arrowstyle='-|>'))
    ax[0].annotate('VP Shed Command Received (NR)',xy=('17 19:55',0),xytext=('17 13:55',1000),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received',xy=('17 06:45',0),xytext=('17 00:45',500),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received (NR)',xy=('17 18:55',0),xytext=('17 13:55',1000),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received (NR)',xy=('17 19:55',0),xytext=('17 13:55',1000),arrowprops=dict(arrowstyle='-|>'))
    ax[0].annotate('VP Shed Command Received',xy=('18 06:45',0),xytext=('18 02:45',500),arrowprops=dict(arrowstyle='-|>'))
    ax[0].annotate('VP Shed Command Received',xy=('18 18:55',0),xytext=('18 13:55',1000),arrowprops=dict(arrowstyle='-|>'))
    ax[0].annotate('VP Shed Command Received (NR)',xy=('18 19:55',0),xytext=('18 13:00',500),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received',xy=('18 06:41',0),xytext=('18 01:30',500),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received',xy=('18 18:55',0),xytext=('18 13:55',1000),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received (NR)',xy=('18 19:55',0),xytext=('18 13:00',500),arrowprops=dict(arrowstyle='-|>'))
    fig.tight_layout()
    #plt.show()
    #plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/ewh/overleaf_figures/ewh_vp_no_load_up_watts_emcb_open.png")
#ewh_vp_vs_log_no_loadup(df1,df2)




ewh_log='/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/ewh_emcb_open_load_up.csv'
ewh_vp='/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/vp_data/ewh_load_up_emcbs_open.csv'


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
    y2 = vp['real-power']* 1000
    fig,ax = plt.subplots(2,figsize=(12,8))
    ax[0].xaxis.set_major_locator(plt.MaxNLocator(30))
    ax[1].xaxis.set_major_locator(plt.MaxNLocator(30))
    ax[0].yaxis.set_major_locator(plt.MaxNLocator(10))
    ax[1].yaxis.set_major_locator(plt.MaxNLocator(10))
    ax[0].plot(x2,y2,label='VP Recorded Data')
    ax[1].plot(x,y,label='WH Station Data')
    ax[1].set_xlabel('timestamp (Hours:Minutes)')
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
    
    ax[0].annotate('VP Shed Command Received',xy=('06:43',0),xytext=('00:48',2000),arrowprops=dict(arrowstyle='-|>'))
    ax[0].annotate('VP Shed Command Received',xy=('18:58',0),xytext=('13:03',2000),arrowprops=dict(arrowstyle='-|>'))
    ax[0].annotate('VP Shed Command Received',xy=('19:58',0),xytext=('13:03',2000),arrowprops=dict(arrowstyle='-|>'))

    ax[0].annotate('Loadup Command Received',xy=('06:18',0),xytext=('00:48',500),arrowprops=dict(arrowstyle='-|>'))
    ax[0].annotate('Loadup Command Received',xy=('18:18',0),xytext=('13:03',500),arrowprops=dict(arrowstyle='-|>'))
 


    ax[1].annotate('VP Shed Command Received',xy=('06:40',0),xytext=('00:50',2000),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received',xy=('18:55',0),xytext=('13:00',2000),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('VP Shed Command Received',xy=('19:56',0),xytext=('13:00',2000),arrowprops=dict(arrowstyle='-|>'))
    
    ax[1].annotate('Loadup Command Received',xy=('06:16',0),xytext=('00:50',500),arrowprops=dict(arrowstyle='-|>'))
    ax[1].annotate('Loadup Command Received',xy=('18:16',0),xytext=('12:26',500),arrowprops=dict(arrowstyle='-|>'))
    
    fig.tight_layout()
    #plt.show()
    plt.savefig("/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/figures/ewh/overleaf_figures/ewh_vp_load_up_watts_emcb_open.png")
ewh_vp_vs_log_loadup(df1,df2)
