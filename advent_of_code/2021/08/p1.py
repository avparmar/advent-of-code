with open('inputs/p1/input.txt') as input:
  inputList = input.read().strip().split("\n")
  input.close()
  
count = 0
for encoding in inputList:
  splitEncoding = encoding.split("|")
  lhs = splitEncoding[0].strip().split()
  rhs = splitEncoding[1].strip().split()
  
  for digit in rhs:
    if (len(digit) in [2, 3, 4, 7]):
      count += 1
print(count)