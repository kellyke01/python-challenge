import os
import csv

budgetcsv = os.path.join("..","Resources","budget_data.csv")

with open(budgetcsv, 'r') as file:

    csvReader = csv.reader(file, delimiter = ',')

    csvHeader = next(file)
total_months = 0

#ProfitLoss = 0
lines = file.readlines()

index0 = total_months
total_months = len(lines)
#index1 = ProfitLoss 

print("Financial Analysis")
print("--------------------------------")
print("Total Months:", total_months)
print("total:")
print("Average Change:")
print("Greatest Increase in Profits:")
print("Greatest Decrease in Profits:")

