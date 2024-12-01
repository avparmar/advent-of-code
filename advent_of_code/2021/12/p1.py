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

def explore(cave, alreadySeen):
  if cave == 'end':
    return 1
  nextPlaces = caves[cave]

  sum = 0
  seenCopy = alreadySeen.copy()
  if cave == cave.lower():
    seenCopy.append(cave)
  for place in nextPlaces:
    if place not in alreadySeen:
      sum += explore(place, seenCopy)
  return sum



print(explore('start', ['start']))
    
