with open('inputs/p1/input.txt') as input:
  inputList = list(input.read().split("\n"))
  input.close()

o2Candidates = inputList.copy()
cO2Candidates = inputList.copy()

o2Winner = ""
cO2Winner = ""

for i in range(12):
  if o2Winner == "":
    nextO2Candidates = []
    oneCounts = 0
    for num in o2Candidates:
      if num[i] == "1":
        oneCounts+=1
    mostCommon = int(2 * oneCounts >= len(o2Candidates))
    for num in o2Candidates:
      if int(num[i]) == mostCommon:
        nextO2Candidates.append(num)
    if len(nextO2Candidates) == 1:
      o2Winner = nextO2Candidates[0]
    else:
      o2Candidates = nextO2Candidates

  if cO2Winner == "":
    nextCO2Candidates = []
    oneCounts = 0
    for num in cO2Candidates:
      if num[i] == "1":
        oneCounts+=1
    mostCommon = int(2 * oneCounts < len(cO2Candidates))
    for num in cO2Candidates:
      if int(num[i]) == mostCommon:
        nextCO2Candidates.append(num)
    if len(nextCO2Candidates) == 1:
      cO2Winner = nextCO2Candidates[0]
    else:
      cO2Candidates = nextCO2Candidates

print(o2Winner, cO2Winner)

o2Final = 0
cO2Final = 0

for i in range(12):
  if o2Winner[11-i] == "1":
    o2Final += 2**i
  if cO2Winner[11-i] == "1":
    cO2Final += 2**i

print(o2Final * cO2Final)
