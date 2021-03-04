# .csv file with ballot ID, name, county, and candidate

# Data to retrieve:
# 1) Total number of votes cast
# 2) A complete list of candidates who received votes
# 3) Total number of votes each candidate received
# 4) Percentage of votes each candidate won
# 5) The winner of the election based on popular vote

import csv
import os

file = os.path.join("repo", "Election-Analysis", "resources", "election_result.csv")

# # open/close file for reference only. Use python with statement
# election_data = open(file, "r")
# election_data.close()
newanalysis = os.path.join("repo", "Election-Analysis", "analysis", "election_analysis.txt")
with open(file) as election_data:
# The with statement ends with a colon, which means we need to indent on the next 
# line, as we did with if-else statements and for loops.

# This is what is getting output when running through terminal!!!!!!!!!!!!!!!!!!!!!!!
# <_io.TextIOWrapper name='resources/election_results.csv' mode='r' encoding='UTF-8'>


# Creating new file in a directory
# Create a filename variable to a direct or indirect path to the file.
    # newanalysis = os.path.join("repo", "Election-Analysis", "analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
    # writeup = open(newanalysis, "w")
    # writeup.write("Automatically add text to a file")
    # writeup.close()
# write data with with statement
    # with open(newanalysis, "w") as txt_file:
        # txt_file.write("Entering text using with statements")
        # # Add more text to file...
        # txt_file.write("Arapahoe")
        # txt_file.write("Denver")
        # txt_file.write("Jefferson")
        # txt_file.write("Arapahoe, Denver, Jefferson")
        # txt_file.write("Arapahoe\nDenver\nJefferson")
        #txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")
    print(election_data)