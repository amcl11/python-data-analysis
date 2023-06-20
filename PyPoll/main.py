import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip / store Header row
    csv_header = next(csvreader)

    # set vote count variable to 0
    vote_count = 0

    # initialise list for list of candidates
    candidates = []

    # Create Dictionary to store vote counts for each candidate
    candidate_votes = {}

    # start loop to count total number of votes, populate names into the candidates list, and sum candidate votes
    for row in csvreader:
        vote_count += 1

        name = row[2]  # add names to candidate list

        if name not in candidates:
            candidates.append(name)
            candidate_votes[name] = 0  # initialise vote count for each candidate to zero

        candidate_votes[name] += 1  # Increment vote count by 1 for the corresponding candidate

    # Define separator and line space strings
    separator = '-' * 30
    line_space = '\n'

    # Create the output string using f-strings and proper formatting
    output = f"""
Election Results \n
{separator} \n
Total Votes: {vote_count} \n
{separator}\n""" 

    # initialise loop to calculate percent of votes for each candidate
    for candidate, votes in candidate_votes.items():
        percent_of_votes = votes / vote_count * 100

        output += f"""
{candidate}: {percent_of_votes:.3f}% ({votes})\n""" 

    # set variables for Max Votes and Winner
    max_votes = 0
    winner = ""

    # initialise loop to find the candidate with the highest vote count
    for candidate, votes in candidate_votes.items():
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    output += f"""
{separator}\n
Winner: {winner}\n
{separator}\n"""

    # Specify location / folder for new analysis txt file
    outpath = os.path.join('analysis', 'PyPoll_Analysis.txt')

    # Write the output to the file
    with open(outpath, 'w') as f:
        f.write(output)

    # Print the output to the console
    print(output)
