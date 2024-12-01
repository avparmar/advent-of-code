import collections

with open('inputs/p1/input.txt') as input:
  inputList = list(map(int, (input.readline().split(","))))
  input.close()

inputList.sort()
crabs = collections.Counter(inputList)
newCrabs = {}
for i in range(1978):
  newCrabs[i] = 0 if i not in crabs.keys() else crabs[i]

ascCrabs = [0] * 1978
totalCrabsAsc = 6
fuelFactorAsc = 6
descCrabs = [0] * 1978
totalCrabsDesc = 1
fuelFactorDesc = 1

for i in range(1978):
  if i != 0:
    ascCrabs[i] = ascCrabs[i-1] + fuelFactorAsc
    totalCrabsAsc += newCrabs[i]
    fuelFactorAsc += totalCrabsAsc
    descCrabs[1977 - i] = descCrabs[1978 - i] + fuelFactorDesc
    totalCrabsDesc += newCrabs[1977 - i]
    fuelFactorDesc += totalCrabsDesc

sums = [ascCrabs[i] + descCrabs[i] for i in range(1978)]

print(min(sums))