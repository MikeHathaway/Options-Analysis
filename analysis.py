import pandas as pd
import csv
import time
from datetime import date
today  = date.today()

#select stock ticker to be studied - work in progress
# raw_input('Enter a Stock ticker, ho: ') + '.csv'

#Open selected option chain
file = open('sune.csv')
csv_file = csv.reader(file)
csv_headings = next(csv_file)
print csv_headings

#initiatilze environment
rownum = 0 
Strike = 0
Bid = 0
Ask = 0
spread = 0
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
	#(row[13])
		
		#row[0:0] = [str(spread)]
		#row.append	
	
#Good tutorial on opening csv: https://newcircle.com/s/post/1572/python_for_beginners_reading_and_manipulating_csv_files 
#Tutorial on manipulating CSV https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html 
