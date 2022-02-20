# with open('american-english.txt', 'r') as dictionaryText:
#  dictionaryList = dictionaryText.read().splitlines()
#  dictionaryList.sort(reverse=True, key=len)
#  print(dictionaryList[0:100])


with open('american-english.txt', 'r') as dictionaryText:
  dictionaryList = dictionaryText.read().splitlines()
  wordLengthDictionary = {}
  
  for item in dictionaryList:
    wordLengthDictionary.update({item : len(item)})

view = sorted(wordLengthDictionary.items(), key = lambda x: x[1], reverse=True)
print(view[0:100])