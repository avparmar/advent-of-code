from collections import defaultdict

with open('inputs/p1/input.txt') as input:
  rows = [x for x in input.read().strip().split("\n")]
  input.close()

template = rows[0]
rules = {}

strptr = 0

for row in rows[2::]:
  if not row:
    continue
  a, b = row.split(' -> ')
  rules[a] = b

#print(template)
for i in range(10):
  strptr = 0
  newStr = template
  for j, char in enumerate(template):
    if j == 0:
      #newStr += char
      continue
    prevChar = template[j-1]
    curr = char
    if prevChar + curr in rules:
      strptr += 1
      #print(j, strptr, newStr[:j-1 + strptr:], rules[prevChar + curr], newStr[j-1+ strptr::], newStr[:j-1 + strptr:] + rules[prevChar + curr] + newStr[j-1+ strptr:])
      newStr = newStr[:j-1 + strptr:] + rules[prevChar + curr] + newStr[j-1+ strptr::]
    else:
      strptr +=0
  #print(newStr)
  template = newStr

#print(newStr)
cts = defaultdict(int)

for char in template:
  cts[char] += 1

print(cts)

3115 - 921