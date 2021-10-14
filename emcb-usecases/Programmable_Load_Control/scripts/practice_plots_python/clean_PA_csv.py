from termcolor import colored, cprint

print(colored('TODO: Add function to plot files\n','yellow'))
print('--------------------------------------------------------------------\n')
print('--------------------------------------------------------------------\n')
print('--------------------------------------------------------------------\n')
print(colored('Recorded files from PA4000 must be downloaded from the Drive first. Once thats done, run this script. This script will do the following:\n','red'))
print(colored('* Move the csv file from the download folder to a specified folder.\n','cyan'))
print(colored('* Remove frequency columns from the file and rename the columns appropriately.\n','cyan'))
print(colored('* Since each water heater uses two 120V lines, there will be two Vrms, Irms, Watts for each water heater. Therefore, the script will sum the watts columns for each WH and append the values to new columns.\n','cyan'))
print('--------------------------------------------------------------------\n')
print('--------------------------------------------------------------------\n')
print('--------------------------------------------------------------------\n')
print(colored("Questions Description\n",'red'))
print(colored("name of the file is the file that you want to move out of the Downloads folder\n",'cyan'))
print(colored("Destination is where you want to put the file so Python can access it (i.e usually in cleaned_pa_files)\n",'cyan'))
print(colored("The name of the new file is the file that will have different headers along with the sum of the HPWH power and EWH power\n",'cyan'))

# Cleaning up the PA csv file

#############################################################################
############################## CODE STARTS HERE #############################
#############################################################################


import argparse as ap
import pandas as pd
import numpy as np
import os
import time


def clean_PA4000(file_path,destination,new_file):
    df = pd.read_csv(file_path,skiprows=10)
    df.columns = ['timestamp','ch1_Vrms1','ch1_Irms1','ch1_watts1','freq1','ch2_Vrms2','ch2_Irms2','ch2_watts2','freq2','ch3_Vrms3','ch3_Irms3','ch3_watts3','freq3','ch4_Vrms4','ch4_Irms4','ch4_watts4','freq4']
    #df.drop(df.columns[df.columns.str.contains('freq')], axis=1, inplace=True)
    df["watts_Sum_HPWH"] = df.loc[:,['ch1_watts1','ch2_watts2']].sum(axis=1)
    df["watts_Sum_EWH"] = df.loc[:,['ch3_watts3','ch4_watts4']].sum(axis=1)
    df.to_csv(destination+new_file,index=False)
    print('Here is a list of file in \n'+destination+'\n.Does file exist? Proceed?')
    os.system('ls '+destination+' | grep .csv')
    ask = input()
    if ask == 'no':
        print(colored('make sure the file is moved from Downloads folder to cleaned_pa_files folder','red'))
        print(colored('Here is a list of the files in cleaned_pa_files folder\n','red'))
        os.system("ls "+destination+" | grep .csv")
        quit()
    else:
        print(colored('Sweet!','yellow'))
    os.system('mv '+file_path+' /Users/midrar/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/Full_Data')

'''
parser = ap.ArgumentParser(description='clean up and filter PA4000 csv files')
parser.add_argument('-f','--file_path',type=str, help='path of the input file from PA4000')
parser.add_argument('-d','--destination',type=str,help='Output file destination')
args = parser.parse_args()
'''


print("What's the name of the file? ")
file_name = input()
print(colored("Is this day1, day2, or day3 data? (Answer 1,2, or 3)",'cyan'))


user = input()
if user == '1':
    destination = '~/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/ewh_hpwh_ELECTRIC/Day1_Data/'
    #print(colored('The file is saved at: ',destination,'cyan'))
elif user == '2':
    destination = '~/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/ewh_hpwh_ELECTRIC/Day2_Data/'
    #print(colored('The file is saved at: ',destination,'cyan'))
else:
    destination = '~/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/ewh_hpwh_ELECTRIC/Day3_Data/'
    #print('\n \n \n The file is save at: \n \n \n',destination)

print(colored('Is the heat pump water heater in Electric mode? (Answer yes or no)','cyan'))
user = input()

if user == 'yes':
    print('The file is saved at:',destination)
else:
    destination = '~/Desktop/EMCB/emcb-usecases/Programmable_Load_Control/Data/hpwh_ewh_hybrid/'
    print('The file is saved at: ',destination)

os.system('mv ~/Downloads/'+file_name+' '+destination)
file_path = destination+file_name
print(colored("Moving the file ...",'yellow'))
time.sleep(2)

print(colored('What would you like to name the new file?','cyan'))
new_file = input()
clean_PA4000(destination+file_name,destination,new_file)
