import csv
import os
csvpath = os.path.join("budget_data.csv')

   
open(csvpath, newline='') as csvfile:
csvreader =.csv.reader(csvfile, delimiter=',')
print(csvreader)

for row in csvreader:
    print(row)
