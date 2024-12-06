from advent_of_code.util.input_tools import get_input_rows, get_int_row

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
perm_i, perm_j = curr
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
    
total = 0
for step in seen:
#for step in ['8, 3']:
    obstacle_coord = get_int_row(step, ',')
    # put an obstacle at _step_ then run it and see if we hit a spot we already went in the same direction.
    cx, cy = perm_i, perm_j
    curr_seen = set()
    direction = 0
    looped = True
    while f'{cx},{cy},{direction}' not in curr_seen:
        #print(f'{cx},{cy},{direction}')
        fx, fy = 0, 0
        if direction == 0:
            fx, fy = cx - 1, cy
        elif direction == 1:
            fx, fy = cx, cy + 1
        elif direction == 2:
            fx, fy = cx + 1, cy
        else:
            fx, fy = cx, cy - 1

        if fx < 0 or fx >= bottom or fy < 0 or fy >= right:
            looped = False
            break
        
        # turn
        if rows[fx][fy] == '#' or (fx == obstacle_coord[0] and fy == obstacle_coord[1]):
            direction = (direction + 1) % 4
            continue
    
        curr_seen.add(f'{cx},{cy},{direction}')
        cx,cy = fx,fy

    total += int(looped)

print(total)