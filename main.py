import os

import csv

election_data_csv = os.path.join('/Users/rorosun/Desktop/python-challenge/PyPoll/Resources', 'election_data.csv')

totalVotes = 0 # total rows (not including the header is the total of votes)

votesPerCandidate = {}

# open up election_data
with open(election_data_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        totalVotes += 1
        if row[2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1   
        

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")

for candidate, votes in votesPerCandidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(votesPerCandidate, key=votesPerCandidate.get)

print(f"Winner: {winner}")

f = open("election_results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(totalVotes))
f.write('\n')
f.write("-------------------------")
f.write('\n')

for candidate, votes in votesPerCandidate.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')

