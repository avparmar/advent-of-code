with open('inputs/p1/input3.txt') as input:
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

def explore(cave, alreadySeen, lucky, book):
  #print(cave, lucky, alreadySeen)
  if cave == 'end':
    print(lucky, book + ['end'])
    #return 1
    paths.append(book + ['end'])
    return
  
  connects = caves[cave]
  sc = alreadySeen.copy()

  if cave == cave.lower():
    sc.append(cave)

  bc = book.copy()

  bc.append(cave)

  sum = 0
  for connect in connects:
    if connect in sc:
      if lucky is None and connect != 'start':
        lucky = connect
      else:
        continue
    #print(cave, lucky, alreadySeen)
    #print()
    #sum += explore(connect, sc, lucky, bc)
    explore(connect, sc, lucky, bc)
  #return sum

#print(explore('start', [], None, []))
explore('start', [], None, [])

s = set()
for path in paths:
  s.add(str(path))
  #print(path)

if len(paths) == len(s):
  print(len(paths))