# #PyPoll challenge

import os
import csv

# Set file paths
file_to_load = os.path.join('Resources', 'election_data.csv')
file_to_output = os.path.join("analysis", "election_results.txt")

# Track various parameters
candidates = []
votes = []

# Read CSV and convert data into columns
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data starting after the header
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])

# Calculate the total number of votes cast
total_votes = len(votes)

# Calculate the number of votes for each candidate
candidate_votes = {}
for candidate in candidates:
    if candidate in candidate_votes:
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate] = 1

# Calculate the percentage of votes for each candidate
candidate_percentages = {}
for candidate, votes in candidate_votes.items():
    percentage = round((votes / total_votes) * 100, 3)
    candidate_percentages[candidate] = percentage

# Determine the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Generate the analysis output
output = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
)

for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    output += f"{candidate}: {percentage}% ({votes})\n"

output += (
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n"
)

# Print the output to the terminal
print(output)

# Export the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)