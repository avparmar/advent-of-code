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
fuelFactorAsc = 0
descCrabs = [0] * 1978
fuelFactorDesc = 0

for i in range(1978):
  if i != 0:
    ascCrabs[i] = ascCrabs[i-1] + fuelFactorAsc + newCrabs[i-1]
    fuelFactorAsc += newCrabs[i-1]

#for i in range(1978):
  if i != 0:
    1977, 1976, 1975
    descCrabs[1977 - i] = descCrabs[1978 - i] + fuelFactorDesc + newCrabs[1978 - i]
    fuelFactorDesc += newCrabs[1978 - i]

  print(1977 - i, newCrabs[1977 - i], descCrabs[1977 - i], fuelFactorDesc)

#sums = [ascCrabs[i] + descCrabs[i] for i in range(1978)]

#print(min(sums))

#for i in range(1978):
  #print(ascCrabs[i], descCrabs[i])