import os
csvpath = os.path.join('C:\Users\cesar\Documents\GitHub\python-challenge\PyBank\budget_data.csv')

with open(csvpath, newline='')as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    for row in csvreader:
        print(row)

