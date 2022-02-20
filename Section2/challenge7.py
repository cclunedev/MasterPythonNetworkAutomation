with open('american-english.txt', 'r') as dictionaryText:
  dictionaryList = dictionaryText.read().splitlines()
  wordLengthDictionary = {}
  
  for item in dictionaryList:
    wordLengthDictionary.update({item : len(item)})

print(wordLengthDictionary)