from collections import UserDict
import requests, json, csv

response = requests.get('https://jsonplaceholder.typicode.com/users')
userList = response.json()

with open ('users.csv', 'w') as csvFile:
  write = csv.writer(csvFile)
  for user in userList:
    row = [user['name'], user['address']['city'],'(' + user['address']['geo']['lat'] + ',' + user['address']['geo']['lng'] + ')', user['company']['name']]
    write.writerow(row)