from collections import defaultdict

with open('inputs/p1/input.txt') as input:
  rows = [x for x in input.read().strip().split("\n")]
  input.close()

template = rows[0]

rules = {}

for row in rows[2::]:
  if not row:
    continue
  a, b = row.split(' -> ')
  rules[a] = b

pairs = defaultdict(int)

for i, char in enumerate(template):
  if i == 0:
    continue
  pairs[template[i-1] + template[i]] += 1

for i in range(40):
  newPairs = defaultdict(int)
  for pair in pairs.keys():
    if pair in rules:
      mid = rules[pair]
      newPairs[pair[0] + mid] += pairs[pair]
      newPairs[mid + pair[1]] += pairs[pair]
  pairs = newPairs

cts = defaultdict(int)
for pair in pairs:
  cts[pair[0]] += pairs[pair]
  #cts[pair[1]] += pairs[pair]
cts['O'] += 1
#print(pairs)
#print(cts)
max = cts['B']
min = cts['B']
for ct in cts.values():
  if ct > max:
    max = ct
  if ct < min:
    min = ct

print(max - min)