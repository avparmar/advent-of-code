from advent_of_code.util.input_tools import get_input_rows

rows = get_input_rows()
right = len(rows[0])
bottom = len(rows)

curr = ()

for i, row in enumerate(rows):
    for j, cell in enumerate(row):
        if cell == '^':
            curr = (i, j)
            break
# N E S W -> 0 1 2 3
direction = 0
seen = set([f'{curr[0]},{curr[1]}'])

for steps in range(10000):
    front = ()
    if direction == 0:
        front = (curr[0] - 1, curr[1])
    elif direction == 1:
        front = (curr[0], curr[1] + 1)
    elif direction == 2:
        front = (curr[0] + 1, curr[1])
    else:
        front = (curr[0], curr[1] - 1)
    
    if front[0] < 0 or front[0] >= bottom or front[1] < 0 or front[1] >= right:
        break
    
    front_item = rows[front[0]][front[1]]
    
    # turn
    if front_item == '#':
        direction = (direction + 1) % 4
        continue
    
    seen.add(f'{front[0]},{front[1]}')
    curr = front
    
print(len(seen))