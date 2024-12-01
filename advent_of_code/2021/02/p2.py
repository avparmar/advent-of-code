horizontal = 0
depth = 0
aim = 0

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
      depth = max(0, depth + aim * mag)
    case "down":
      aim+=mag
    case "up":
      aim-=mag

print(horizontal * depth)