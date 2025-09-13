import csv

file_path = r"C:\Users\devah\Documents\PWP\data.csv"

with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


