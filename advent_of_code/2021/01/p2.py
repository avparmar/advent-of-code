with open('inputs/p1/input.txt') as input:
  
  inputList = list(map(int, input.read().split("\n")))
  input.close()
  
increases = 0

window = [inputList[0], inputList[1], inputList[2]]
prevWindow = sum(window)
for i, measurement in enumerate(inputList):
  if i < 2:
    continue
  window.pop(0)
  window.append(measurement)
  currWindow = sum(window)

  if currWindow > prevWindow:
    increases+=1
  prevWindow = currWindow
    
print(increases)
  