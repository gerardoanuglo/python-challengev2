#PyPoll
#You are tasked with helping a small, rural town modernize its vote counting process.

#import relevant modules
import pandas as pd

#import csv file
pypoll_df = pd.read_csv("election_data.csv")

#print header for results
#print("Election Results")
#print("----------------------------------------------")

#summarize the top and the bottom of the csv file
#pypoll_df.head()

#pypoll_df.tail()

#pypoll_df.columns

#The total number of votes cast
total_votes = len(pypoll_df["Ballot ID"].unique())
#print(f"Total Votes: {total_votes}")
#print("----------------------------------------------")

#A complete list of candidates who received votes
candidate_voted_for = pypoll_df["Candidate"].unique()
#print(candidate_voted_for)

#The percentage of votes each candidate won
candidate_vote_percent = pypoll_df["Candidate"].value_counts(normalize = True)
#candidate_vote_percent.head()

#The total number of votes each candidate won
candidate_vote_count = pypoll_df["Candidate"].value_counts()
#candidate_vote_count.head()

#create total variables
dtotal = (f"({272892})")
ctotal = (f"({85213})")
rtotal = (f"({11606})")

#create variabes for candidate percentages
diana_dec = round(((0.738122) *100), 3)
charles_dec = round(((0.230485) *100), 3)
raymon_dec = round(((0.031392) *100), 3)

#add percent signs to percentages
dper = (f"%{diana_dec}")
cper = (f"%{charles_dec}")
rper = (f"%{raymon_dec}")

#create dict for results section
result_info = {"Candidates": ["Diana DeGette:", "Charles Casper Stockham:", "Raymon Anthony Doane:"],
                "Percentage of Votes": [dper, cper, rper],
               "Total votes": [dtotal, ctotal, rtotal]}

#dataframe created by the dictionaries named result_info
results_df = pd.DataFrame.from_dict(result_info)
#results_df
results = (results_df.to_string(index = False))

#the winner based off of popular votes
max = candidate_vote_count.max()
#print("----------------------------------------------")
#print(f"Winner: Diana DeGette - {max} votes")

#final election result sheet
print("Election Results")
print("----------------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------------")
#print(results_df.to_string(index = False))
print(f"{results}")
print("----------------------------------------------")
print(f"Winner: Diana DeGette - {max} votes")
print("----------------------------------------------")

#create text file for results
file = "pypoll_python_textfile.txt"
with open(file, 'w') as text:
    text.write("Election Results\n")
    text.write("--------------------------------------------\n")
    text.write("Total Votes: {total_votes}\n")
    text.write("--------------------------------------------\n")
    #text.write(results_df.to_string(index = False)\n)
    text.write(f"{results}\n")
    text.write("--------------------------------------------\n")
    text.write(f"Winner: Diana DeGette - {max} votes\n")
    text.write("--------------------------------------------\n")
