import collections

with open('inputs/p1/input.txt') as input:
  inputList = list(map(int, (input.readline().split(","))))
  input.close()

inputList.sort()
crabs = collections.Counter(inputList)
crabsRev = collections.Counter(inputList[::-1])

spots = len(crabs.keys())
ascCrabs = [0] * spots
prevAscCrabs = 6
prevAscCoord = 0
descCrabs = [0] * spots
prevDescCrabs = 1
prevDescCoord= 1977

for i, k in enumerate(crabs.keys()):
  if i != 0:
    ascCrabs[i] = (k - prevAscCoord) * prevAscCrabs + ascCrabs[i-1]
    prevAscCrabs += crabs[k]
    prevAscCoord = k
  
for i, k in enumerate(crabsRev.keys()):
  if i != 0:
    descCrabs[i] = (prevDescCoord - k) * prevDescCrabs + descCrabs[i-1]
    prevDescCrabs += crabsRev[k]
    prevDescCoord = k

sums = [ascCrabs[i] + descCrabs[spots - i - 1] for i in range(spots)]

print(min(sums))