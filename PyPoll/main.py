# ## Option 2: PyPoll

# ![Vote-Counting](Images/Vote_counting.jpg)

# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# You will be given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`). Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# * The total number of votes cast

# * A complete list of candidates who received votes

# * The percentage of votes each candidate won

# * The total number of votes each candidate won

# * The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

# ```
# Election Results
# -------------------------
# Total Votes: 620100
# -------------------------
# Rogers: 36.0% (223236)
# Gomez: 54.0% (334854)
# Brentwood: 4.0% (24804)
# Higgins: 6.0% (37206)
# -------------------------
# Winner: Gomez
# -------------------------
# ```

# Your final script must be able to handle any such similarly-structured dataset in the future (i.e you have zero intentions of living in this hillbilly town -- so your script needs to work without massive re-writes). In addition, your final script should both print the analysis to the terminal and export a text file with the results.


import os
import csv

from collections import defaultdict

my_dict = defaultdict(int)
total_votes = 0



filepath = os.path.join("raw_data", "election_data_2.csv")

with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
         total_votes += 1
         my_dict[row["Candidate"]] = my_dict.get(row["Candidate"], 0) + 1
         



wfilepath = os.path.join("raw_data", "results.txt")
with open(wfilepath,"w+") as writer:

    writer.write("Election Results\n")
    writer.write("-" * 28)
    writer.write(f"\nTotal Votes: {total_votes}\n")
    writer.write("-" * 28)
    for key, value in my_dict.items() :
        writer.write (f"\n{key}")
        writer.write("\t{:.0%}".format(value/total_votes))
        writer.write(f"\t{value}\n")
    writer.write("-" * 28)
    writer.write(f"\nWinner: {max(my_dict.items())[0]}\n")

    writer.write("-" * 28)

    writer.seek(0) #points file back to beginning before printing
    print(writer.read())
