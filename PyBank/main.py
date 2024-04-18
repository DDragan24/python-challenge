import os
import csv

main_csv = os.path.join("..","PyBank", "Resources", "budget_data.csv")
dataFile = os.path.join("Financial_Analysis.txt")
netChangelist = []
BestIncrease = ["", 0]
WorstDecrease = ["", 0]
with open(main_csv) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    csvHeader = next(csvReader)
    firstRow = next(csvReader)
    previousNet = int(firstRow[1])
    # print(firstRow)               - test to see what firstRow ouptuts
    # print(previousNet)            - test to see what previousNet outputs
    
    months = []
    totalChange = 0
    
    for row in csv.reader(csvFile,):
        months.append(row[0])
        totalChange += float(row[1])
        netChange = int(row[1]) - previousNet
        previousNet = int(row[1])
        netChangelist += [netChange]

        BestIncrease = [months[0], netChangelist[0]]
        WorstDecrease = [months[0], netChangelist[0]]

average = sum(netChangelist) / len(netChangelist)

for m in range(len(netChangelist)):
    if(netChangelist[m] > BestIncrease[1]):
        BestIncrease[1] = netChangelist[m]
        BestIncrease[0] = months[m]
    if(netChangelist[m] < WorstDecrease[1]):
        WorstDecrease[1] = netChangelist[m]
        WorstDecrease[0] = months[m]

data = (
    f"\nFinancial Analysis\n"
    f"===================================== \n"
    f"\tTotal Months: {len(months)} \n"
    f"\tTotal Profit/Losses: {totalChange} \n"
    f"\tAverage Change: ${average:.2f} \n"
    f"\tGreatest increase in Profits: {BestIncrease[0]}, {BestIncrease[1]} \n"
    f"\tGreatest decrease in Profits: {WorstDecrease[0]}, {WorstDecrease[1]} \n"
)
print(data)

with open(dataFile, "w") as textFile:
    textFile.write(data)