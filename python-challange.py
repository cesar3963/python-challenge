import csv
import os

    csvpath = os.path.join('python-challenge','budget_data.csv')
   
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvpath, delimiter=',')
    date = 0
    for row in csvreader:
        print(', '.join(row))
