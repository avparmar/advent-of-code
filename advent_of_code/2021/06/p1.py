with open('inputs/p1/input.txt') as input:
  inputList = list(map(int, (input.readline().split(","))))
  input.close()

fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for entry in inputList:
  fish[entry] += 1

for i in range(80):
  newFish = fish[0]
  for j in range(8):
    fish[j] = fish[j+1]
  fish[6] += newFish
  fish[8] = newFish

print(sum(fish))
