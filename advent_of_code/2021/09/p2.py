with open('inputs/p1/input.txt') as input:
  rows = [list(map(int, x.strip())) for x in input.readlines()]
  input.close()

lows = []

for i, row in enumerate(rows):
  for j, col in enumerate(row):
    count = 0
    if j == 0 or row[j-1] > col:
      count += 1
    if j == 99 or row[j+1] > col:
      count += 1
    if i == 0 or rows[i-1][j] > col:
      count += 1
    if i == 99 or rows[i+1][j] > col:
      count += 1
    if count == 4:
      lows.append((i,j))

basins = []

def expand(i, j):
  if (i, j) in path:
    return 0
  if rows[i][j] == 9:
    return 0
  path.append((i, j))
  sum = 0
  val = rows[i][j]
  if i != 0:
    sum += expand(i-1, j)
  if i != 99:
    sum += expand(i+1, j)
  if j != 0:
    sum += expand(i, j-1)
  if j != 99:
    sum += expand(i, j+1)

  return sum + 1

for low in lows:
  path = []
  basins.append(expand(low[0], low[1]))

top3 = []
m1 = -1
for basin in basins:
  m1 = max(m1, basin)
top3.append(m1)
basins.remove(m1)

m1 = -1
for basin in basins:
  m1 = max(m1, basin)
top3.append(m1)
basins.remove(m1)

m1 = -1
for basin in basins:
  m1 = max(m1, basin)
top3.append(m1)
basins.remove(m1)

print(top3[0] * top3[1] * top3[2])