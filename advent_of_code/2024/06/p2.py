from advent_of_code.util.input_tools import get_input_rows, get_int_row

"""
NOTE: This doesn't work atm
"""

#rows = get_input_rows()
rows = get_input_rows('alt_input.txt')
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
seen = {f'{i},{j},0': 0}
collisions = list()
coll_count = 0


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
        collisions.append(f'{curr[0]},{curr[1]},{direction}')
        coll_count += 1
        direction = (direction + 1) % 4
        continue
    
    seen[f'{front[0]},{front[1]},{direction}'] = coll_count
    print(f'{front[0]},{front[1]},{direction},{coll_count}')
    curr = front

count = 0
# work backwards from each collision 
for coll_ind, collision in enumerate(collisions):
#for coll_ind, collision in enumerate(['6,2,3']):
    coll_coord = get_int_row(collision, ',')
    print("collision: ", coll_coord)
    coord_dir = coll_coord[2]
    walking_from_dir = (coll_coord[2] - 1) % 4
    # head south
    if coord_dir == 0:
        ind = coll_coord[0] + 1
        while ind < bottom:
            if rows[ind][coll_coord[1]] == '#':
                break
            if f'{ind},{coll_coord[1]},{walking_from_dir}' in seen and seen[f'{ind},{coll_coord[1]},{walking_from_dir}'] >= coll_ind:
                print(f'obstacle idea: {ind},{coll_coord[1]},{walking_from_dir}')
                count += 1
            ind += 1
    # head west
    elif coord_dir == 1:
        ind = coll_coord[1] - 1
        while ind >= 0:
            if rows[coll_coord[0]][ind] == '#':
                break
            if f'{coll_coord[0]},{ind},{walking_from_dir}' in seen and seen[f'{coll_coord[0]},{ind},{walking_from_dir}'] >= coll_ind:
                print(f'obstacle idea: {coll_coord[0]},{ind},{walking_from_dir}')
                count += 1
            ind -= 1
    # head north
    elif coord_dir == 2:
        ind = coll_coord[0] - 1
        while ind >= 0:
            #print(f'{ind},{coll_coord[1]},{walking_from_dir}')
            if rows[ind][coll_coord[1]] == '#':
                break
            if f'{ind},{coll_coord[1]},{walking_from_dir}' in seen and seen[f'{ind},{coll_coord[1]},{walking_from_dir}'] >= coll_ind:
                print(f'obstacle idea: {ind},{coll_coord[1]},{walking_from_dir}')
                count += 1
            ind -= 1
    # head east
    else:
        ind = coll_coord[1] + 1
        while ind < right:
            #print(coll_coord[0], ind, 2)
            if rows[coll_coord[0]][ind] == '#':
                break
            if f'{coll_coord[0]},{ind},{walking_from_dir}' in seen and seen[f'{coll_coord[0]},{ind},{walking_from_dir}'] >= coll_ind:
                print(f'obstacle idea: {coll_coord[0]},{ind},{walking_from_dir}')
                count += 1
            ind += 1
            
print(count)
#print(collisions)
print("actual ones:\n","[8, 1, 3] -> 8,7,2\n", "[1, 4, 0] -> 6,4,3 & 8,4,3\n", "[4, 2, 0] -> 8,2,3\n", "[8, 6, 2] -> 7,6,1\n", "[6, 2, 3] -> 6,6,2\n")

#print("check result:",f'6,6,2' in seen, other_dirs_not_in_seen(6,6,2))