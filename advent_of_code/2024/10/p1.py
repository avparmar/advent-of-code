from advent_of_code.util.input_tools import InTool
from collections import defaultdict

it = InTool()

rows = it.get_int_grid(digit=True)

connected = defaultdict(set)

def update_peaks_from_coord(i: int, j: int, height: int):
    key = f'{i},{j}'
    adj = it.get_adjacent(i, j)
    if height == 8:
        for c in adj:
            if rows[c[0]][c[1]] == 9:
                connected[key].add(c)
    else:
        for c in adj:
            if rows[c[0]][c[1]] == height + 1:
                connected[key].update(connected[f'{c[0]},{c[1]}'])
            
        

for target in range(8, -1, -1):
    for i, row in enumerate(rows):
        for j, height in enumerate(row):
            if height == target:
                update_peaks_from_coord(i, j, height)
            
total = 0

for i, row in enumerate(rows):
    for j, height in enumerate(row):
        if height == 0:
            total += len(connected[f'{i},{j}'])
        
print(total)
