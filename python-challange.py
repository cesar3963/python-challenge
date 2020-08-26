import csv

with open('budget_data.csv', 'r')as budget:

    csv_reader = csv.reader(budget)
    print(csv_reader)
       
    for row in csv_reader:
        profits = sum("Profit/Losses")

        print(profits)
    
