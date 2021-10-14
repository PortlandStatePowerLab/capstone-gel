import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
'''
ewh_log="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/Noloadup_emcb_closed.csv"
df3 = pd.read_csv(ewh_log,parse_dates=True)

x1 = pd.to_datetime(df3.iloc[:,0])
x1 = pd.to_datetime(x1)
x1 = x1.dt.strftime('%H:%M')
y1 = df3['real_available_Wh']
y2 = df3['consumed_watts']
fig = plt.figure(figsize=(12,4))
ax1 = fig.add_subplot(111)
ax1.plot(x1,y1,label='EnergyTake (Wh)')
ax1.set_xlabel("timestamp")
plt.title('Closed EMCB:HPWH No LoadUp Command Sent')
ax1.set_ylabel("EnergyTake (Wh)")
ax1.xaxis.tick_bottom()
ax1.yaxis.tick_left()
ax1.tick_params(axis='x')
ax1.tick_params(axis='y')
y_max = df3['real_available_Wh'].max()
plt.ylim([0,y_max])
ax1.xaxis.set_major_locator(plt.MaxNLocator(40))
ax1.xaxis.tick_bottom()
ax1.yaxis.tick_left()
plt.xticks(rotation=45)
ax2 = ax1.twinx()
fig.subplots_adjust(bottom=0.2)
ax2.plot(x1,y2,color='r',label='Real Power (W)')
ax2.set_ylabel('Real Power (W)')
ax2.xaxis.set_major_locator(plt.MaxNLocator(40))
fig.legend(loc='upper right',bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
y2_max = df3['consumed_watts'].max()
plt.ylim([0,y2_max])
plt.grid()

plt.show()
    #plt.savefig("/Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/log_files/ewh/csv_logs/figures/ewh_LoadUp_emcb_closed_log.eps")
'''

ewh_log="/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/hpwh_logs/hpwh_loadup_emcb_closed.csv"
df3 = pd.read_csv(ewh_log,parse_dates=True)

x1 = pd.to_datetime(df3.iloc[:,0])
x1 = pd.to_datetime(x1)
x1 = x1.dt.strftime('%H:%M')
y1 = df3['real_available_Wh']
y2 = df3['consumed_watts']
fig = plt.figure(figsize=(12,4))
ax1 = fig.add_subplot(111)
ax1.plot(x1,y1,label='EnergyTake (Wh)')
ax1.set_xlabel("timestamp")
plt.title('Closed EMCB:HPWH LoadUp Command Sent')
ax1.set_ylabel("EnergyTake (Wh)")
ax1.xaxis.tick_bottom()
ax1.yaxis.tick_left()
ax1.tick_params(axis='x')
ax1.tick_params(axis='y')
y_max = df3['real_available_Wh'].max()
plt.ylim([0,y_max])
ax1.xaxis.set_major_locator(plt.MaxNLocator(40))
ax1.xaxis.tick_bottom()
ax1.yaxis.tick_left()
plt.xticks(rotation=45)
ax2 = ax1.twinx()
fig.subplots_adjust(bottom=0.2)
ax2.plot(x1,y2,color='r',label='Real Power (W)')
ax2.set_ylabel('Real Power (W)')
ax2.xaxis.set_major_locator(plt.MaxNLocator(40))
fig.legend(loc='upper right',bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
y2_max = df3['consumed_watts'].max()
plt.ylim([0,y2_max])
plt.grid()

plt.show()

