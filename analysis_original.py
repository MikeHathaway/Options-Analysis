import pandas as pd
import numpy as np
import csv
import time
from datetime import date
today  = date.today()

#select stock ticker to be studied - work in progress
# raw_input('Enter a Stock ticker, ho: ') + '.csv'

#Open selected option chain
file = open('sune.csv')
csv_file = csv.reader(file)
file_headers = next(csv_file)
print file_headers

#initiatilze environment
rownum = 0 
Strike = 0
Bid = 0
Ask = 0
spread = 0
#open_interest = row[11]
potential_options = []
#MVP Option = 0 - Identify a specific option in the chain based upon favorable characteristics

#Analyze key chain parameters - Add put call ratio later
#def bid_ask_spread(Call, Put, Strike, Bid, Ask):
for row in csv_file:
	Bid = float(row[6])
	Ask = float(row [7])
	spread = Ask - Bid
	row[13:13] = [str(spread)]
	row.append(row[13:13])
	print row
	
def spread_analysis(spread, open_interest):
	for row in csv_file:
		if float(spread) >= 0.2: # and Open_Interest > raw_input :
			del row
		else:
			print row
	return spread

print spread_analysis	

my_writer = csv.DictWriter(file, fieldnames=file_headers)

#GOAL: screen the option chain for options that meet certain characteristics (certain bid ask spread, ratio, open interest)	
	
#Good tutorial on opening csv: https://newcircle.com/s/post/1572/python_for_beginners_reading_and_manipulating_csv_files 
#Tutorial on manipulating CSV https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html 
