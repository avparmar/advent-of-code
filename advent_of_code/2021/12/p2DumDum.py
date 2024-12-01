with open('inputs/p1/input.txt') as input:
  rows = [x for x in input.read().strip().split("\n")]
  input.close()

caves = {}

for row in rows:
  coords = row.split('-')
  if coords[0] in caves.keys():
    caves[coords[0]].append(coords[1])
  else:
    caves[coords[0]] = [coords[1]]
  if coords[1] in caves.keys():
    caves[coords[1]].append(coords[0])
  else:
    caves[coords[1]] = [coords[0]]

#print(caves)
#print(rows)

paths = []

def explore(cave, alreadySeen, lucky, luckySeen, path):
  #print("->",cave)
  #if cave == 'end' and luckySeen == 0:
    #return 0
  path1 = path.copy()
  path1.append(cave)
  if cave == 'end' and path1 not in paths:
    paths.append(path1)
    return 1
  nextPlaces = caves[cave]

  sum = 0
  seenCopy = alreadySeen.copy()
  if cave == lucky:
    if luckySeen >= 1:
      seenCopy.add(cave)
    else:
      luckySeen += 1
  if cave == cave.lower() and cave != lucky:
    seenCopy.add(cave)


  for place in nextPlaces:
    if place not in alreadySeen:
      sum += explore(place, seenCopy, lucky, luckySeen, path1)
  return sum

bigSum = 0
smalls = []
for cave in caves.keys():
  if cave != 'start' and cave != 'end' and cave == cave.lower():
    smalls.append(cave)

#print(smalls)

for smal in smalls:
  bigSum += explore('start', set('start'), smal, 0, [])
print(bigSum)
    
#print(paths)
