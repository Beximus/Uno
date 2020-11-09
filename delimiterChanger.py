import csv

reader = csv.reader(open("verysmall.csv", "rU"), delimiter=',')
writer = csv.writer(open("output.txt", 'w'), delimiter=';')
writer.writerows(reader)

print("Delimiter successfully changed")