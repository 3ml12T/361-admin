import csv

def categorize(row):


with open('data/11_37_53_30_6_2022.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar='"')
    for row in data:
        categorize(row)