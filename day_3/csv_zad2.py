import csv

# filename = 'records.csv'
filename = 'records_discount.csv'

fields = []
rows = []

with open(filename, "r") as csv_f:
    csvreader = csv.reader(csv_f, delimiter=";")
    print(csvreader)  # <_csv.reader object at 0x000002C8D6EA08E0>

    fields = next(csvreader)  # odczyta jeden wiersz, ustawi odczyt na nastepny

    for row in csvreader:
        rows.append(row)

print("Fields:", fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['radek', 'coe', '3', '0']]
# ['6;today;200']]
#  ['6', 'today', '200']
