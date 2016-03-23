#build an arrow debrue model
#for probability states, use open interest as a % of total open interest
import pandas as pd
import numpy as np
import csv


#Open selected option chain as a dataframe
option_data = pd.read_csv('sune.csv')
option_data.columns = pd.Series(option_data.columns).str.replace(' ','_')

#calculate each options fraction of open interest: probability states
#NEED TO GROUP BY EXPIRY: Similar hedging and investment practices expected per period for open interest
option_data['fraction_oi']= option_data['Open_Interest'].div(option_data['Open_Interest'].sum()) * 100

#expected future price of underlying
future_price = raw_input('Expected future price of underlying: ')
future_price = float(future_price)

#Conditionals to determine payoff for each option, given expected future price
def payoff(value):
	if option_data['Option_Type'] == 'Call':
		future_price - option_data['Strike']

option_data['payoff'] = 

print future_price


print option_data.head()





#http://synesthesiam.com/posts/an-introduction-to-pandas.html 