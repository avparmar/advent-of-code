with open('inputs/p1/input.txt') as input:
  inputList = list(input.read().split())
  input.close()

pairs = list(zip(map(lambda item: list(map(int, item.split(","))), inputList[::3]), map(lambda item: list(map(int, item.split(","))),inputList[2::3])))

hits = {}
for pair in pairs:
  if pair[0][0] != pair[1][0] and pair[0][1] != pair[1][1]:
    continue
  if pair[0][0] == pair[1][0]:
    for i in range(min(pair[0][1], pair[1][1]), max(pair[0][1], pair[1][1])+1):
      if (pair[0][0], i) in hits:
        hits[(pair[0][0], i)] += 1
      else:
        hits[(pair[0][0], i)] = 1

  elif pair[0][1] == pair[1][1]:
    for i in range(min(pair[0][0], pair[1][0]), max(pair[0][0], pair[1][0])+1):
      if (i, pair[0][1]) in hits:
        hits[(i, pair[0][1])] += 1
      else:
        hits[(i, pair[0][1])] = 1

count = 0
for key in hits:
  if hits[key] > 1:
    count+=1

print(count)