import string

with open('american-english.txt', 'r') as dictionaryText:
  letterCount = {}
  for c in string.ascii_lowercase:
    letterCount[c] = 0
  
  for line in dictionaryText.read():
    for char in line:
      if char in string.ascii_lowercase:
        letterCount.update({char.lower(): letterCount[char.lower()] + 1})
      
      
view = sorted(letterCount.items(), key = lambda x: x[1], reverse=True)
print(view[0:3])