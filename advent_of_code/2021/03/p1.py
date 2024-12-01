with open('inputs/p1/input.txt') as input:
  inputList = list(input.read().split("\n"))
  input.close()

gammaBinaryCounts = [0] * 12

for i in range(12):
    for num in inputList:
      if num[i] == "1":
        gammaBinaryCounts[i]+=1

gamma = 0
epsilon = 0

for i in range(12):
  if gammaBinaryCounts[11-i] > 500:
    gamma += 2**i
  else:
    epsilon += 2**i

print(gamma * epsilon)

