# .csv file with ballot ID, name, county, and candidate

# Data to retrieve:
# 1) Total number of votes cast
# 2) A complete list of candidates who received votes
# 3) Total number of votes each candidate received
# 4) Percentage of votes each candidate won
# 5) The winner of the election based on popular vote

import csv
import os

file = os.path.join("resources", "election_result.csv")

# # open/close file for reference only. Use python with statement
# election_data = open(file, "r")
# election_data.close()

with open(file) as election_data:
# The with statement ends with a colon, which means we need to indent on the next 
# line, as we did with if-else statements and for loops.

# This is what is getting output when running through terminal!!!!!!!!!!!!!!!!!!!!!!!
# <_io.TextIOWrapper name='resources/election_results.csv' mode='r' encoding='UTF-8'>





    print(election_data)