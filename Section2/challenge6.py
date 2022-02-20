def compareLines(txtName1, txtName2):
  with open(txtName1, 'r') as txt1:
    with open(txtName2, 'r') as txt2:
      list1 = txt1.read().splitlines()
      list2 = txt2.read().splitlines()
      
      for i in range(len(list1)):
        if list1[i] != list2[i]:
          print(list1[i] + '\n' + list2[i])


compareLines('banking.txt','banking2.txt')