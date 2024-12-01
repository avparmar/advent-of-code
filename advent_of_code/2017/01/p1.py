with open('input.txt') as input:
    sequence = input.read().strip()
    input.close()

sum = 0

for ind in range(len(sequence)):
    if int(sequence[ind]) == int(sequence[ind-1]):
        sum += int(sequence[ind])
        
        
print(sum)