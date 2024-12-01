with open('inputs/p1/input.txt') as input:
  rows = input.read().strip().split("\n")
  input.close()

sum = 0

history = [5]

for row in rows:
  oldsum = sum
  for char in row:
    if char == '(':
      history.append(0)
    elif char == '[':
      history.append(1)
    elif char == '{':
      history.append(2)
    elif char == '<':
      history.append(3)
    else:
      temp = history.pop()
      if char == ')':
        if temp != 0:
          sum += 3
          break
      elif char == ']':
        if temp != 1:
          sum += 57
          break
      elif char == '}':
        if temp != 2:
          sum += 1197
          break
      elif char == '>':
        if temp != 3:
          sum += 25137
          break

print(sum)