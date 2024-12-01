from collections import defaultdict

with open('inputs/p1/input.txt') as input:
  rows = [x for x in input.read().strip().split("\n")]
  input.close()

coords = set()

folds = []

for row in rows:
  if not row:
    continue
  if row[0] == 'f':
    if row.find('x') == -1:
      folds.append(('y', int(row[row.find('=') + 1:])))
    else:
      folds.append(('x', int(row[row.find('=') + 1:])))
  else:
    a, b = row.split(',')
    coords.add((int(a), int(b)))

#print(len(coords))
for fold in folds:
  if fold[0] == 'y':
    newCoords = set()
    for coord in coords:
      #print(coord)
      newY = coord[1]
      #print("fold:", folds[0][1])
      #print("y:", coord[1])
      if coord[1] > fold[1]:
        newY = fold[1] + fold[1] - coord[1]
      #print("->", (coord[0], newY))
      newCoords.add((coord[0], newY))
    coords = newCoords
  else:
    newCoords = set()
    for coord in coords:
      #print(coord, folds[0][1])
      newX = coord[0]
      if coord[0] > fold[1]:
        newX = fold[1] + fold[1] - coord[0]
      #print("->", (newX, coord[1]))
      newCoords.add((newX, coord[1]))
    coords = newCoords

#print(coords)
#print(len(coords))

for x in range(7):
  ps = ""
  for y in range(40):
    if (y,x) in coords:
      ps += "#"
    else:
      ps += " "
    ps += " "
  print(ps)