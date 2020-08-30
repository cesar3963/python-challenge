import os
import csv


csvpath = os.path.joim("..","csv", "budget_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)
    print(f"csv header: {csv_header}")

    for row in csvreader:
        print(row)
