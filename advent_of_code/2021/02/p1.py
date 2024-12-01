horizontal = 0
depth = 0

with open('inputs/p1/input.txt') as input:
  inputList = list(input.read().split("\n"))
  input.close()

for line in inputList:
  command = line.split(" ")
  op = command[0]
  mag = int(command[1])
  match op:
    case "forward":
      horizontal+=mag
    case "down":
      depth+=mag
    case "up":
      depth = max(0, depth-mag)

print(horizontal * depth)