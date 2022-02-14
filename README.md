# Election_Analysis
##Project Overview
The Colorado Baord of Elections has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
* Data Source: election_results.csv
* Software: Python 3.7.6, Visual Studio Code 1.57.1

## Results Summary
The analysis of the election show that:

* There were 369,711 votes cast in the election.
* Breakdown by county:
  * Jefferson county had 38,855 votes (10.5 %)
  * Denver county had 306,066 votes (82.8%)
  * Arapahoe county had 24,801 (6.7%)
* The candidates were
  *   Charles Casper Stockham
  *   Diana DeGette
  *   Raymon Anthony Doane
* The candidate results were:
  * Charles Casper Stockham received 23% of the vote and 85,213 votes.
  * Diana DeGette received 73.8% of the vote and 272,892 votes.
  * Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
* The winner of the election was:
  * Diana Degette, who received 73.8% of the vote and 272,892 votes!

## Audit Summary

This python script can be used to produce an equivalent analysis with the results printed in the official election analysis output summary. If the source csv file is formatted the same as the source provided, then the analysis can be run without changes. However, if there are some differences, the script can be altered in a few minor ways to accomodate the difference without reformatting the source dataset. The following lines of code, which appear on lines 51 and 54, can be changed to read the appropriate columns in a csv file.


candidate_name = row[2]

county_name = row[1]


These two lines fetch the candidate's name and the county's name respectively. Changing the number within the brackets will read the appropriate column in the dataset. If the source dataset is formatted in the same way only two lines need to be changed in order to read from and write to the approriate files.


file_to_load = os.path.join("Resources", "election_results.csv")


For this line (line 9), simply replace the words within quotes with the source file and its parent folder. On the next line, the procedure will be very similar. Here is the code for line 11:


file_to_save = os.path.join("analysis", "election_analysis.txt")


Just as before, change the words within quotes to the file that sould be written to and its parent folder. Once these changes are made, the script will be ready to run a thorough analysis and audit of any election.
