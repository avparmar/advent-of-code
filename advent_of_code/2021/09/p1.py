with open('inputs/p1/input.txt') as input:
  rows = [list(map(int, x.strip())) for x in input.readlines()]
  input.close()

sum = 0

for i, row in enumerate(rows):
  for j, col in enumerate(row):
    count = 0
    if j == 0 or row[j-1] > col:
      count += 1
    if j == 99 or row[j+1] > col:
      count += 1
    if i == 0 or rows[i-1][j] > col:
      count += 1
    if i == 99 or rows[i+1][j] > col:
      count += 1
    if count == 4:
      sum += col + 1
print(sum)