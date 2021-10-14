import pandas as pd
import csv

file_path = '/Users/midrar/Desktop/EMCB/emcb-usecases/DER_Data_2021-07-19.log'
timestamp = []
import_power = []
file = open(file_path,'r')
lines = file.read().splitlines()


