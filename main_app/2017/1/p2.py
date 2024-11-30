with open('input.txt') as input:
    sequence = input.read().strip()
    input.close()

sum = 0
step = len(sequence) // 2

for ind in range(len(sequence)):
    if int(sequence[ind]) == int(sequence[(ind + step) % len(sequence)]):
        sum += int(sequence[ind])
        
        
print(sum)