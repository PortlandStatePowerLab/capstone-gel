# Created by Midrar Adham
# Summer Term 2021
# midrar.adhm@gmail.com

####################################################
####################################################

import pandas as pd
from datetime import datetime
from datetime import timedelta

#path ='/home/parallels/Desktop/emcb-use-cases/Programmable_Load_Control/Data/final_logs/ewh_logs/vp_data/ewh_no_load_up_emcb_open_aug17_18.csv'
#df = pd.read_csv(path)


# # Function creates timestamp column.

# Credits: Stackoverflow
def create_timestamp(length):			# When calling this function, pass the length of the timestamp in minutes. (1 day = 1440 minutes)
	time_str = '2021-08-17 00:00:00'				# starting date.
	date_format_str = '%Y-%m-%d %H:%M:%S'			# timestamp format
    given_time = datetime.strptime(time_str, date_format_str)
    timestamp = []
    for length in range(0,length):					# length is the number of minutes in a day
        final_time = given_time + timedelta(minutes=length)
        final_time_str = final_time.strftime('%Y-%m-%d %H:%M:%S')
        timestamp.append(final_time_str)
    df = pd.DataFrame(timestamp)					# create a dataframe for the new time stamp
    df.to_csv('two_days_one_min.csv',index=False,header=False)
    #df.to_csv("/Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/log_files/hpwh/csv_logs/vp_data/one_minute.csv",index=False,header=False)
    return df
df1 = create_timestamp(120)
print(df1)
