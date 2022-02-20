import time

def tail(textFileName, number):
  with open(textFileName, 'r') as txtFile:
    txtString= txtFile.read()
    return txtString[-number:]

while True:
  t = tail('sample_file.txt', 53)
  print(t)
  time.sleep(3)
