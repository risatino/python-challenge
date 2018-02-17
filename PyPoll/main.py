# Dependencies
import os
import csv

# File Path
csvpath1 = os.path.join('Resources', 'election_data_1.csv')
csvpath2 = os.path.join('Resources', 'election_data_1.csv')

# Variables
vote_count = 0
candidates = {}
candidates_percent = {}
winner = ""
winner_count = 0

# Read File
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)

    # Find total vote count and individual vote count
    for row in csvreader:
        vote_count += 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

# % for each candidate
for key, value in candidates.items():
    candidates_percent[key] = round((value/vote_count) * 100, 2)

# find the winner
for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

# TESTING
# print(total_vote_count)
# print(candidates)
# print(candidates_percent)
# print(winner)

# printing to the terminal
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(vote_count))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

# create new csv file
new_file = open("Reports/results.csv", "w")

# write the new file
new_file.write("Election Results \n")
new_file.write("------------------------------------- \n")
new_file.write("Total Votes: " + str(vote_count) + "\n")
new_file.write("------------------------------------- \n")
for key, value in candidates.items():
    new_file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
new_file.write("------------------------------------- \n")
new_file.write("Winner: " + winner + "\n")
new_file.write("------------------------------------- \n")