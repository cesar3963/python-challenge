import csv
import os

csvpath = os.path.joim("..", "csv", "budget_data.csv")


with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:count(row)
        print(row)