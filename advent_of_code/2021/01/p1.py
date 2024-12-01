with open('inputs/p1/input.txt') as input:
  inputList = input.read().split("\n")
  input.close()
  
increases = 0

for i, measurement in enumerate(inputList):
  if i == 0:
    continue
  if int(inputList[i]) > int(inputList[i-1]):
    increases+=1
print(increases)
    
  