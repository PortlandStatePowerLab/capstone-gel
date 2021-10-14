# This scrips is used to plot GridLAB-D output files in particular and other files in general. It cleans up the timezone associated with timestamp column, change the time format to hours:minutes, and set image format to eps which is best for overleaf documentation.

import pandas as pd
import datetime
import matplotlib.pyplot as plt




# Call the function and pass the path of the input file and the path of where the figure should be saved along with the name of the image.

. 
def gld_plot(file_path,figure_path):
    df = pd.read_csv(file_path,skiprows=8)

    df['# timestamp'].str.replace('UTC','')

    df['# timestamp'] = pd.to_datetime(df['# timestamp'])

    df['# timestamp'] = df['# timestamp'].dt.strftime('%H:%M')

    print(df['# timestamp'])

    ax = df.plot(x = '# timestamp',y = 'power.real',title='EWH GLD Model',colormap='jet',grid=1)

    ax.set_xlabel('timestamp')

    ax.set_ylabel('power (kW)')

    #plt.show()

    plt.savefig(figure_path+'.eps',format='eps')

def plot_PA_data(file_path1,file_path2,save_path):
'''    
    print("First file path: \n")

    x = input()

    print("Second file path: \n")

    y = input()

    print("path and name of the image: \n")

    z = input()
'''
    df = pd.read_csv(file_path1)

    df2 = pd.read_csv(file_path2)

    # convert df timestamp object to datetime

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Change the format from YYYY-MM-DD HH:MM:SS to HH:MM

    df['timestamp'] = df['timestamp'].dt.strftime('%H:%M')

    # convert df timestamp object to datetime

    df2['time'] = pd.to_datetime(df2['time'])

    # Change the format from YYYY-MM-DD HH:MM:SS to HH:MM

    df2['time'] = df2['time'].dt.strftime('%H:%M')


    fig = plt.figure()
    
    ax = fig.add_subplot(111, label="1")
    
    ax2 = fig.add_subplot(111,label="2",frame_on=False)

    ax.plot(df['timestamp'],df['watts_Sum_HPWH'],color='r')

    ax.set_xlabel("timestamp_PA",color='r')

    ax.set_ylabel("real Power (W)",color='r')

    ax.xaxis.tick_bottom()

    ax.yaxis.tick_left()

    ax.tick_params(axis='x',color='r')

    ax.tick_params(axis='y',color='r')
    
    ax.xaxis.set_major_locator(plt.MaxNLocator(9))
    
    ax2.xaxis.set_major_locator(plt.MaxNLocator(9))
    
    ax2.plot(df2['time'],df2['real-power'],color='b')
    
    ax2.xaxis.tick_top()
    
    ax2.yaxis.tick_right()

    ax2.set_xlabel('timestamp_VP',color='b')

    ax2.set_ylabel('Real Power (kW)',color='b')
    
    ax2.xaxis.set_label_position('top')
    
    ax2.yaxis.set_label_position('right')
    
    ax2.tick_params(axis='x', colors="b")
    
    ax2.tick_params(axis='y', colors="b")
    
    plt.savefig(save_path+'.eps',format='eps')
'''
print("plot GLD file: \n")

x = input()

print("Second file path: \n")

y = input()

print("path and name of the image: \n")

z = input()

plot_PA_data(x,y,z)
'''




