import csv
import os

main_csv = os.path.join("..","Pypoll", "Resources", "election_data.csv")
dataFile = os.path.join("BallotAnalysis.txt")

totalBallots = 0
candidates = []
ballots = {}
winningCount = 0
winner = ""
with open(main_csv) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    csvHeader = next(csvFile)
    
    
    for row in csvReader:
        totalBallots += 1

        if row[2] not in candidates:
            candidates.append(row[2])

            ballots[row[2]] = 1
        else:
            ballots[row[2]] += 1

voteOutput = ""            
for candidates in ballots:
     votes = ballots.get(candidates) 
     votePCT = (float(votes) / float(totalBallots)) * 100.00
     voteOutput += f"\t{candidates}: {votePCT:.2f}% ({int(votes)}) \n"

     if votes > winningCount:
        winningCount = votes
        winner = candidates

winnerData = f"Winner: {winner}"

data = (

    f"\nElection Results\n"
    f"-------------------------------------\n"
    f"\tTotal Votes: {totalBallots}\n"
    f"-------------------------------------\n"
    f"\n{voteOutput}\n"
    f"-------------------------------------\n"
    f"\t{winnerData}\n"
    f"-------------------------------------\n"

)

print(data)
with open(dataFile, "w") as textFile:
    textFile.write(data)