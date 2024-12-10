from advent_of_code.util.input_tools import InTool

it = InTool()

rows = it.get_int_grid(digit=True)

connected = {}

def update_peaks_from_coord(i: int, j: int, height: int):
    adj = it.get_adjacent(i, j)
    total = 0
    if height == 8:
        for c in adj:
            if rows[c[0]][c[1]] == 9:
                total += 1
    else:
        for c in adj:
            if rows[c[0]][c[1]] == height + 1:
                total += connected[f'{c[0]},{c[1]}']
    connected[f'{i},{j}'] = total            
        

for target in range(8, -1, -1):
    for i, row in enumerate(rows):
        for j, height in enumerate(row):
            if height == target:
                update_peaks_from_coord(i, j, height)
            
total = 0

for i, row in enumerate(rows):
    for j, height in enumerate(row):
        if height == 0:
            total += connected[f'{i},{j}']
        
print(total)
