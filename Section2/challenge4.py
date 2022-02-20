def wordCount(textFileName):
  with open(textFileName, 'r') as txtFile:
    
    lineList = txtFile.read().splitlines()
    print('Number of Lines: ' + str(len(lineList)))
    
    txtFile.seek(0)
    wordList = txtFile.read().split()
    print('Number of Words: ' + str(len(wordList)))

    txtFile.seek(0)
    characters = txtFile.read()
    print('Number of Characters: ' + str(len(characters)))




wordCount('sample_file.txt')