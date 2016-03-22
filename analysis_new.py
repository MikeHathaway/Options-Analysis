import pandas as pd
import numpy as np
import csv
import time
from datetime import date
today  = date.today()

#http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/    <- pandas tutorial 

#select stock ticker to be studied - work in progress
# raw_input('Enter a Stock ticker, ho: ') + '.csv'

#Open selected option chain as a dataframe
option_data = pd.read_csv('sune.csv')
option_data.columns = pd.Series(option_data.columns).str.replace(' ','_')

#define bid ask spread and apply spread column to dataframe
option_data['spread'] = (option_data['Ask'] - option_data['Bid']).astype(float) 

#print option_data.head()
#filter data for favorable characteristics
filtered_data = option_data[option_data['spread'] <= 0.2]

#generate data frame with only relevant information
relevant_columns = ['Expire_Date','Bid','Ask','spread','Implied_Volatility','Open_Interest']
filtered_data = filtered_data[relevant_columns]

print filtered_data.head()

#print option_data[relevant_columns].head()

#option_data[relevant_columns].to_csv('modified_sune.csv')



'''
#Screen rows based upon characteristics of bid/ask spread
potential_options = spread < .2

#GOAL: screen the option chain for options that meet certain characteristics (certain bid ask spread, ratio, open interest)'''