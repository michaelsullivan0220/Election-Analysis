# Election Analysis

Write algorithms that will assist the confirmation and analysis of election results.

## Election Audit Results

- The total number of votes cast in the election is `369,711`. Since each row represents one vote, as the algorithm loops through, it will increases a `total_votes` variable by one. This variable was set to zero before the loop started.

    ```py
    for row in reader:
       total_votes = total_votes + 1
    ```

## County Summary

- The total percentage and number of votes per county are as follows:  

    ```
    Jefferson: 10.5% with 38,855 votes.
    Denver: 82.8% with 306,055 votes.
    Arapahoe: 6.7% with 24,801 votes.
    ```

    The counties are added to a list named `counties_list` by checking every row to see if the county associated with that row is already in the counties list or not listed yet. If it is not listed, it will append (add) the county name to the list and set its vote count to zero, then add 1 to the total to capture that rows vote. If it is already listed, it will jump right to adding the vote to the total.

    ```py
    if county_name not in county_options :
            
        county_options.append(county_name)
        counties_votes[county_name] = 0

    counties_votes[county_name] += 1
    ```

- The county with the most votes, was **Denver** county with **306,055** votes. 

## Candidate Summary

- The breakdown of votes by candidate can be seen below:

    ```
    Charles Casper Stockham: 23.0% with 85,213 votes.
    Diana DeGette: 73.8% with 272,892 votes.
    Raymon Anthony Doane: 3.1% with 11,606 votes.
    ```

    The method to retrieve these values is similar to tallying the votes by county value. The algorithm will check to see if the candidate name associated that row is already in the `candidate_options` list. If it is not listed, it will append (add) the candidate's name to the list and set its vote count to zero, then add 1 to the total to capture that rows vote. If it is already listed, it will jump right to adding the vote to the total for that candidate.

    ```
    if candidate_name not in candidate_options:

        candidate_options.append(candidate_name)
        candidate_votes[candidate_name] = 0

    candidate_votes[candidate_name] += 1
    ```

## Winning Candidate

- The winning candidate was **Diana DeGette**. This candidate received 73.8% of the vote with **272,892** total votes.

## Election Audit Summary

Although this algorithm was designed for this specific election, the code can be modified to audit other elections as well.

- In the event that more counties, states or other areas need to be accounted for across multiple .csv files, this algorithm can be modified to compile all the data into one election-results.txt. Adding a WITH statement to open and read another .csv file and the same IF statements can add analyze and add the data to existing variables.

- In addition to reading multiple files, additional IF statements can be added to calculate results for propositional votes that are typically included on election ballots. These votes are usually 'Yes' or 'No' and can be tallied by initializing a variable (i.e. prop_405) to zero before looping and adding or skipping based on the result of an IF statement.
