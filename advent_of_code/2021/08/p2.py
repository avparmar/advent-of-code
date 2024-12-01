with open('inputs/p1/input.txt') as input:
  inputList = input.read().strip().split("\n")
  input.close()
  
sum = 0
for encoding in inputList:
  splitEncoding = encoding.split("|")
  lhs = splitEncoding[0].strip().split()
  rhs = splitEncoding[1].strip().split()
  inDigits = [""] * 10
  sixNineZero = []
  twoThreeFive = []

  for digit in lhs:
    if len(digit) == 2:
      inDigits[1] = digit
    if len(digit) == 4:
      inDigits[4] = digit
    if len(digit) == 3:
      inDigits[7] = digit
    if len(digit) == 7:
      inDigits[8] = digit
    if len(digit) == 5:
      twoThreeFive.append(digit)
    if len(digit) == 6:
      sixNineZero.append(digit)

  for digit in sixNineZero:
    #print(set(inDigits[4]), set(digit))
    if set(inDigits[4]).issubset(set(digit)):
      inDigits[9] = digit
    elif set(inDigits[7]).issubset(set(digit)):
      inDigits[0] = digit
    else:
      inDigits[6] = digit

  for digit in twoThreeFive:
    if set(inDigits[7]).issubset(set(digit)):
      inDigits[3] = digit
    elif set(digit).issubset(set(inDigits[9])):
      inDigits[5] = digit
    else:
      inDigits[2] = digit

  num = ""
  #print(rhs)
  for digit in rhs:
    for i, idk in enumerate(inDigits):
      #print(digit, i, idk)
      if set(idk) == set(digit):
        num += str(i)
        break
  #print(num)
  sum += int(num)
print(sum)