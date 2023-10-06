import os
import csv
electioncsv = os.path.join("..","Resources", "election_data.csv")

print(electioncsv)
with open(electioncsv, 'r', encoding = "utf=8") as csvfile:
    #split reader object
    csvReader = csv.reader(csvfile, delimiter = ",")
    #grabheader
    csvHeader = next(csvReader)

    print(cvsHeader)
#for Row in csvReader:
    #if row[0] = Ballots:
    #print(f"len{BallotNumbers}")

