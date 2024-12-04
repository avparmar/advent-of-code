from advent_of_code.util.input_tools import get_input_rows

rows = get_input_rows()

right = len(rows[0])
bottom = len(rows)

def nw_mas(coord):
    if coord[0] - 3 < 0 or coord[1] - 3 < 0:
        return 0
    return int(rows[coord[0] - 1][coord[1] - 1] == 'M' and rows[coord[0] - 2][coord[1] - 2] == 'A' and rows[coord[0] - 3][coord[1] - 3] == 'S')

def ne_mas(coord):
    if coord[0] - 3 < 0 or coord[1] + 3 >= right:
        return 0
    return int(rows[coord[0] - 1][coord[1] + 1] == 'M' and rows[coord[0] - 2][coord[1] + 2] == 'A' and rows[coord[0] - 3][coord[1] + 3] == 'S')

def se_mas(coord):
    if coord[0] + 3 >= bottom or coord[1] + 3 >= right:
        return 0
    return int(rows[coord[0] + 1][coord[1] + 1] == 'M' and rows[coord[0] + 2][coord[1] + 2] == 'A' and rows[coord[0] + 3][coord[1] + 3] == 'S')

def sw_mas(coord):
    if coord[0] + 3 >= bottom or coord[1] - 3 < 0:
        return 0
    return int(rows[coord[0] + 1][coord[1] - 1] == 'M' and rows[coord[0] + 2][coord[1] - 2] == 'A' and rows[coord[0] + 3][coord[1] - 3] == 'S')

total = 0
for i, row in enumerate(rows):
    if i == 0 or i == bottom - 1:
        continue
    for j, letter in enumerate(row):
        if j == 0 or j == right - 1:
            continue
        if letter == 'A':
            total += int(((se_mas((i - 2, j - 2))) or nw_mas((i + 2, j + 2))) and (sw_mas((i - 2, j + 2)) or ne_mas((i + 2, j - 2))))
            
#print(nw_mas((2,2)))
print(total)