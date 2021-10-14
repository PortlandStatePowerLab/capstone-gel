import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

ewh_log ="/Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/log_files/ewh/csv_logs/DER_Data_2021-07-29.csv"
ewh_vp ='/Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/log_files/ewh/csv_logs/vp_data/VP_29_ewh.csv'
cols = ['timestamp','idk1','idk2','idk3','idk4','element_rated_watts','available_energy','rated_available_energy','real_watts','op_state']
df3 = pd.read_csv(ewh_log,names=cols,parse_dates=True)
df4 = pd.read_csv(ewh_vp,parse_dates=True)

def ewh_plots(df3,df4):
	x1 = pd.to_datetime(df3.iloc[:,0])
	x1 = pd.to_datetime(x1)
	x1 = x1.dt.strftime('%H:%M')
	y1 = df3['available_energy']
	fig = plt.figure(figsize=(12,4))
	ax1 = fig.add_subplot(111)
	ax1.plot(x1,y1)
	ax1.set_xlabel("timestamp")
	plt.title('Closed EMCB:EWH Received LoadUp Command')
	ax1.set_ylabel("EnergyTake (Wh)")
	ax1.xaxis.tick_bottom()
	ax1.annotate('load up command received',xy=('06:15',1650),xytext=(0,15),arrowprops=dict(arrowstyle='-|>'))
	ax1.annotate('load up command received',xy=('18:44',375),xytext=(1000,1200),arrowprops=dict(arrowstyle='-|>'))
	ax1.yaxis.tick_left()
	ax1.tick_params(axis='x')
	ax1.tick_params(axis='y')
	y_max = df3['available_energy'].max()
	plt.ylim([0,y_max])
	ax1.xaxis.set_major_locator(plt.MaxNLocator(40))
	ax1.xaxis.tick_bottom()
	ax1.yaxis.tick_left()
	fig.subplots_adjust(bottom=0.2)
	plt.xticks(rotation=45)
	plt.savefig("/Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/log_files/ewh/csv_logs/figures/ewh_LoadUp_emcb_closed_log.eps")


	x2 = pd.to_datetime(df4['time'])
	x2 = pd.to_datetime(x2)
	x2 = x2.dt.strftime('%H:%M')
	y2 = df4['real-power'].multiply(1000)
	fig = plt.figure(figsize=(12,4))
	ax2 = fig.add_subplot(111)
	ax2.plot(x2,y2)
	ax2.set_xlabel("timestamp")
	plt.title('Closed EMCB:EWH Received LoadUp Command VP')
	ax2.set_ylabel("Real Power (W)")
	ax2.xaxis.tick_bottom()
	# ax.annotate('load up command received',xy=('03:25',1500),xytext=(0,15),arrowprops=dict(arrowstyle='-|>'))
	ax2.yaxis.tick_left()
	ax2.tick_params(axis='x')
	ax2.tick_params(axis='y')
	ax2.xaxis.set_major_locator(plt.MaxNLocator(40))
	plt.xticks(rotation=45)
	y_max = y2.max()
	plt.ylim([0,y_max+3])
	fig.subplots_adjust(bottom=0.2)
	# plt.show()
	plt.savefig("/Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/log_files/ewh/csv_logs/figures/ewh_LoadUp_emcb_closed_vp.eps")
ewh_plots(df3,df4)


hpwh_log ="/Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/log_files/hpwh/csv_logs/DER_Data_2021-07-29.csv"
hpwh_vp ='/Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/log_files/hpwh/csv_logs/vp_data/VP_29.csv'
cols = ['timestamp','rated_available_energy','op_state','idk1','rated_imported_energy','real_imported_energy','available_energy','idk2','idk3','idk4']
df1 = pd.read_csv(hpwh_log,names=cols,parse_dates=True)
df2 = pd.read_csv(hpwh_vp,parse_dates=True)


def hpwh_plots(df1,df2):
	x1 = pd.to_datetime(df1.iloc[:,0])
	x1 = pd.to_datetime(x1)
	x1 = x1.dt.strftime('%H:%M')
	y1 = df1['available_energy']
	fig = plt.figure(figsize=(12,4))
	ax1 = fig.add_subplot(111)
	ax1.plot(x1,y1)
	ax1.set_xlabel("timestamp")
	plt.title('Closed EMCB:HPWH Received LoadUp Command')
	ax1.set_ylabel("EnergyTake (Wh)")
	ax1.xaxis.tick_bottom()
	ax1.annotate('load up command received',xy=('03:25',1500),xytext=(0,15),arrowprops=dict(arrowstyle='-|>'))
	ax1.yaxis.tick_left()
	ax1.tick_params(axis='x')
	ax1.tick_params(axis='y')
	y_max = df1['available_energy'].max()
	plt.ylim([0,y_max])
	ax1.xaxis.set_major_locator(plt.MaxNLocator(40))
	ax1.xaxis.tick_bottom()
	ax1.yaxis.tick_left()


	fig.subplots_adjust(bottom=0.2)
	plt.xticks(rotation=45)
	plt.savefig("/Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/log_files/hpwh/csv_logs/figures/hpwh_LoadUp_emcb_closed_log.eps")
	x2 = pd.to_datetime(df2['time'])
	x2 = pd.to_datetime(x2)
	x2 = x2.dt.strftime('%H:%M')
	y2 = (df2['real-power'].multiply(1000))
	fig = plt.figure(figsize=(12,4))
	ax2 = fig.add_subplot(111)
	ax2.plot(x2,y2)
	ax2.set_xlabel("timestamp")
	plt.title('Closed EMCB:HPWH Received LoadUp Command VP')
	ax2.set_ylabel("Real Power (kW)")
	ax2.xaxis.tick_bottom()
	# ax.annotate('load up command received',xy=('03:25',1500),xytext=(0,15),arrowprops=dict(arrowstyle='-|>'))
	ax2.yaxis.tick_left()
	ax2.tick_params(axis='x')
	ax2.tick_params(axis='y')
	ax2.xaxis.set_major_locator(plt.MaxNLocator(40))
	plt.xticks(rotation=45)
	y_max = y2.max()
	plt.ylim([0,y_max])
	fig.subplots_adjust(bottom=0.2)
	# plt.show()
	plt.savefig("/Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/log_files/hpwh/csv_logs/figures/hpwh_LoadUp_emcb_closed_vp.eps")
# hpwh_plots(df1,df2)

