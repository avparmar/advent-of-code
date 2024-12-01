with open('inputs/p1/input.txt') as input:
  rows = [list(map(int,[char for char in x])) for x in input.read().strip().split("\n")]
  input.close()

#print(rows)

def raiseAdj(i, j):
  tryRaise(i-1, j)
  tryRaise(i+1, j)
  tryRaise(i, j-1)
  tryRaise(i, j+1)
  tryRaise(i-1, j+1)
  tryRaise(i+1, j+1)
  tryRaise(i-1, j-1)
  tryRaise(i+1, j-1)
  
def tryRaise(i, j):
  if (i != -1 and i != 10) and (j != -1 and j != 10) and rows[i][j] != 0:
    rows[i][j] += 1


sum = 0

for k in range(100):
  for i, row in enumerate(rows):
    for j, char in enumerate(row):
      row[j] += 1

  #print(rows)

  cont = 100
  while cont != 0:
    cont = 100
    for i, row in enumerate(rows):
      for j, char in enumerate(row):
        if char > 9:
          sum += 1
          row[j] = 0
          raiseAdj(i, j)
        else:
          cont -= 1

print(sum)

