with open('inputs/p1/input.txt') as input:
  rows = input.read().strip().split("\n")
  input.close()

sum = 0

history = [5]
newRows = []

for row in rows:
  nope = False
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
          nope = True
          break
      elif char == ']':
        if temp != 1:
          nope = True
          break
      elif char == '}':
        if temp != 2:
          nope = True
          break
      elif char == '>':
        if temp != 3:
          nope = True
          break
  if not nope:
    newRows.append(row)

scores = []
l = len(newRows)
for row in newRows:
  xx = []
  sc = 0
  for char in row:
    if char == '(':
      xx.append(1)
    elif char == '[':
      xx.append(2)
    elif char == '{':
      xx.append(3)
    elif char == '<':
      xx.append(4)
    else:
      xx.pop()
  for char in xx[::-1]:
    sc = (sc * 5) + char
    #print(sc)
  scores.append(sc)

scores.sort()

print(scores[(l // 2)])
