# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_result.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter and list and dictionary
total_votes = 0
candidate_options = []
candidate_votes = {}


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
     # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

    # Print the total votes and candidates list
    print("")
    print("Total Votes")
    print(total_votes)
    print("")
    print("Candidates")
    print(candidate_options)
    print("")
 


