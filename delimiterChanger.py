import csv

reader = csv.reader(open("abcde.csv", "rU"), delimiter=',')
writer = csv.writer(open("abcde.txt", 'w'), delimiter=';')
writer.writerows(reader)

print("Delimiter successfully changed")