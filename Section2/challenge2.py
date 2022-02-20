def tail(textFileName, number):
  with open(textFileName, 'r') as txtFile:
    txtString= txtFile.read()
    return txtString[-number:]

t = tail('sample_file.txt', 53)
print(t)
