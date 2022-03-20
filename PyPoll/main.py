# Import os module to create file paths across operating systems
import os

# Import csv module to read imported csv file
import csv

# Create dictionary to sum data by candidate
votetotals = {}

# Create list for assembling ballots by candidate name
ballots = []

# Create list for assembling candidates' summary data
candidate_sum = []

# Create list for storing the results of our analysis
resultslist = []

# Store file path to csv study file as variable
votes_csv = os.path.join("Resources", "election_data.csv")

# Open our csv file and separate data using comma delimiter
with open (votes_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    # Skip the header row (no figures for calculation)
    csvheader = next(csvreader)

    # Cycle through all rows 
    for rows in csvreader:    
        
        #... and create one dictionary key for each candidate, initial vote count set at '0'
        votetotals[rows[2]] = 0
        #... and assemble votes by candidate name in our ballot list
        ballots.append(rows[2])

# While looping through each candidate in our dictionary
for candidate in votetotals:

    # ...loop through all ballots
    for ballot in ballots:

        #...and increase the value for each candidate's key value (ballot count) for each vote
        if ballot == candidate:
            votetotals[ballot] = int(votetotals[ballot]) + 1
    
    # Assemble percent/total and total votes in the summary candidate table
    candidate_sum.append(f"{candidate}: {round((int(votetotals[candidate])/len(ballots)*100),3)}% ({votetotals[candidate]})")

# Calculate the winner
winner = max(votetotals, key=votetotals.get) 

# Store assembled reporting data to a list for our analysis tables
resultslist.append("Election Results")
resultslist.append("-------------------------")
resultslist.append(f"Total Votes : {len(ballots)}")
resultslist.append("-------------------------")
resultslist.extend(candidate_sum)
resultslist.append("-------------------------")
resultslist.append(f"Winner: {winner}")
resultslist.append("-------------------------")

# Store file path for our txt analysis file as variable
results_txt = os.path.join("Analysis", "results.txt")

# Export our analysis list to the txt file
with open (results_txt, 'w') as textfile:
    for results in resultslist:
        textfile.write(results)
        textfile.write('\n')

# Print our analysis list to the terminal
for results in resultslist:
    print(results)