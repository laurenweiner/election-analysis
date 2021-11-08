# The data we need to retrieve. 
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

#Assign a variable for the file to load and the path
#I know this isn't the right code, but I think since I'm already in that folder, it wasn't working.
file_to_load = "election_results.csv"

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")

#initalize total votes variable and set to 0
total_votes=0

#initialize candidate options list
candidate_options=[]

#initialize candidate:votes dictionary
candidate_votes={}

#initialize Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file 
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #for each row, add to total vote count
    for row in file_reader:
        total_votes+=1

    #get the candidate name list 
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            
            #add the candidate name to the list 
            candidate_options.append(candidate_name)

            #begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
            
            #begin tracking the candidates vote count
        candidate_votes[candidate_name] += 1

#print(candidate_votes)

    #use for loop to iterate through candidate options list 
    for candidate_name in candidate_votes:

        #retrieve votes of candidate from candidate votes dictionary
        votes = candidate_votes[candidate_name]

        #calculate percentage of votes and format % to 1 decimal place
        vote_percentage = float(votes) / float(total_votes) *100
        f_vote_percentage = "{:.1f}".format(vote_percentage)

        #print candidate name and % of votes
        print(f"{candidate_name}: {f_vote_percentage}% ({votes:,})\n")
    
        #determine the winning vote count and candidate
        #1. determine if the voes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            #2. if true, set winning count=votes and winning_percent=vote percent
            winning_count = votes
            winning_percentage = vote_percentage

            #3. set winning candidate equal to candidates name 
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"--------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------\n")
    
    print(winning_candidate_summary)