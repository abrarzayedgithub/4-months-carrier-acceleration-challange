import csv
with open('dict.csv',"r") as f:
    dict = csv.DictReader(f)

    for row in dict:
        print(row)