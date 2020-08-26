import csv

with open('pythong_challenge', 'pybank', 'budget_data.csv', 'r')as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    for row in csvreader:
        print(row)

