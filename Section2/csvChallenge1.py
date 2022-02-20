import csv
people = [['Dan', 34, 'Bucharest'],['Andrei',21, 'London'],['Maria', 45, 'Paris']]

with open('people1.csv', 'w') as csvFile:
  writer = csv.writer(csvFile)
  writer.writerows(people)

with open('people1.csv', 'r') as csvFile:
  listTwo = []
  reader = csv.reader(csvFile)
  for row in reader:
    listTwo.append(row)

print(listTwo)