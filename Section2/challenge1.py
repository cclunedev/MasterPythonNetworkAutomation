from operator import concat


with open('sample_file.txt', 'r') as txtFile:
  txtList = txtFile.read().splitlines()
  for row in txtList:
    print(row)
  txtString = "\n".join(txtList)
  print(txtString)