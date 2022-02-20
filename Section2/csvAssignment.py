import csv

devices = []
with open('devices.txt', 'r') as csvFile:
  reader = csv.reader(csvFile, delimiter=':')
  for row in reader:
    devices.append(row)

print(devices)