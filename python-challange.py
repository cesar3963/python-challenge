import csv
import os
csvpath = os.path.join('PyBank','budget_data.csv')

   
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvpath, delimiter=',')
    print(csvreader)

for row in csvreader:
    print(row)
