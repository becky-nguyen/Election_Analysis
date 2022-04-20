#Add our dependencies
import csv
import os
#Assign a variable for the file to load from a path.
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#Initialize the total vote counter
total_votes = 0 
#Initialize Candidate Options list
candidate_options = []
#Initialize Candidate Votes dictionary
candidate_votes = {}
#Initialize winning variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]
        #Remove duplicate candidate names
        if candidate_name not in candidate_options:
            #Add the candidate name to the list
            candidate_options.append(candidate_name)
            #Begin tracking the candidate's vote count
            candidate_votes [candidate_name] = 0
            #Add one for each candidate if their name shows up
        candidate_votes [candidate_name] += 1
with open(file_to_save, "w") as txt_file:

#Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)
    
    #3.5.4 Determine the percentage of votes for each candidate by looping through the counts
    #1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes)*100
        #4. Print the candidate name and percentage of votes

    #To do: print out each candidate's name, vote count, and percentage of votes to the terminal
        #print (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        
    #3.5.5 Winning Candidate and Winning Count Tracker

    #Determine winning vote count and candidate
    #1. Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. If true then the set winning_count=votes and winning_percent=vote_percentage
            winning_count = votes 
            winning_percentage = vote_percentage
            #3. Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
    #To do: print out the winning candidate, vote count, and percentage to 
    #terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #save winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
