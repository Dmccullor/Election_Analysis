#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the elction based on popular vote
#6. Determine the eliminated candidate for each round of voting
#7. When the candidate wins a majority (+50%) that candidate is the winner

#Add our depdencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "rc_election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("Resources", "rc_election_analysis.txt")

#Declare eliminated candidates list
eliminated_candidates = []

# Function to add up the votes and skip to the next column for eliminated candidates
def vote_retrieval(*eliminated_candidates):
    #Initialize a total vote counter.
    total_votes = 0
    #Candidate options and candidate votes
    candidate_options = []
    candidate_votes = {}
    # Open the election results and read the file.
    with open(file_to_load, 'r') as election_data:
        #Read the file object with the reader function.
        file_reader = csv.reader(election_data)
        #Read the header row.
        headers = next(file_reader)
        #Print each row in the CSV file.
        for row in file_reader:
            round = 0
            #Add to the total vote count.
            total_votes += 1
            #Get the candidate name for each row.
            candidate_name = row[2]
            #If the candidate is eliminated read the candidate from the next round column
            while candidate_name in eliminated_candidates:
                round +=1
                candidate_name = row[2 + round]
            #If the candidate does not match any existing cnadidate add it to the candidate list.
            if candidate_name not in candidate_options:
                #Add the candidate name to the candidate list.
                candidate_options.append(candidate_name)
                #And begin tracking that candidate's voter count.
                candidate_votes[candidate_name] = 0
            #Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1
    
    return total_votes, candidate_votes, candidate_options

#Asssign output variables to an initial run of function to get a number of candidates to loop through
total_votes, candidate_votes, candidate_options = vote_retrieval()
#Assign the number of candidates to a separate variable
num_of_candidates = len(candidate_options)

#Function to determine the winner and eliminated candidates
def winner_calculation(total_votes, candidate_votes):
    #Declare our tracking variables
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
    eliminated_candidate = ""
    lowest_percentage = 0
    #Loop through dictionary of candidates and their vote totals
    for candidate_name in candidate_votes:
        #Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        #Determine winning vote count, winning percentage and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        #Determine the lowest percentage and add assign that candidate to eliminated candidate variable
        if lowest_percentage == 0 and vote_percentage >= 0:
            eliminated_candidate = candidate_name
            lowest_percentage = vote_percentage
        elif vote_percentage < lowest_percentage:
            eliminated_candidate = candidate_name
            lowest_percentage = vote_percentage    
        else:
            pass
    
    return winning_count, winning_percentage, winning_candidate, eliminated_candidate


#Loop through candidates
#Add the eliminated candidate to the list of eliminated candidates for each round
for i in range(num_of_candidates):
    total_votes, candidate_votes, candidate_options = vote_retrieval(eliminated_candidates)
    winning_count, winning_percentage, winning_candidate, eliminated_candidate = winner_calculation(total_votes, candidate_votes)
    #Add the eliminated candidate from each round to the global eliminated candidates list
    eliminated_candidates.append(eliminated_candidates)
    #break the loop when the winning percentage is above 50%
    if winning_percentage > 50:
        break

#Write the election results to external text file
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)

    #Loop through the candidates to print their vote totals
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        #Print each candidate, their voter count, and percentage to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,} votes)\n")
        print(candidate_results)
        #Save the candidate results to our text file.
        txt_file.write(candidate_results)

    #Print the winning candidates' results to the terminal.
    winning_candidate_summary =(
            f"---------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)