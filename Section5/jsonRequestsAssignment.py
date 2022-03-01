import requests, json

response = requests.get('https://jsonplaceholder.typicode.com/todos')
toDoList = response.json()

print(type(toDoList))

for tattoo in toDoList:
  if tattoo['completed'] == True:
    print(tattoo)
