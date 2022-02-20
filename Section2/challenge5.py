def accountCalc(transactionFileName):
  actValue = 0
  with open(transactionFileName, 'r') as transactions:
    for line in transactions:
      if line[0] == str('D'):
        actValue += int(line[2:])

      elif line[0] == 'W':
        actValue -= int(line[2:])

    print(actValue)


accountCalc('banking.txt')
      
  