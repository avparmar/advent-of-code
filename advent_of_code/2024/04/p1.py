from advent_of_code.util.input_tools import get_input_rows

rows = get_input_rows()

right = len(rows[0])
bottom = len(rows)

def nw_mas(coord):
    if coord[0] - 3 < 0 or coord[1] - 3 < 0:
        return 0
    return int(rows[coord[0] - 1][coord[1] - 1] == 'M' and rows[coord[0] - 2][coord[1] - 2] == 'A' and rows[coord[0] - 3][coord[1] - 3] == 'S')

def n_mas(coord):
    if coord[0] - 3 < 0:
        return 0
    return int(rows[coord[0] - 1][coord[1]] == 'M' and rows[coord[0] - 2][coord[1]] == 'A' and rows[coord[0] - 3][coord[1]] == 'S')

def ne_mas(coord):
    if coord[0] - 3 < 0 or coord[1] + 3 >= right:
        return 0
    return int(rows[coord[0] - 1][coord[1] + 1] == 'M' and rows[coord[0] - 2][coord[1] + 2] == 'A' and rows[coord[0] - 3][coord[1] + 3] == 'S')

def e_mas(coord):
    if coord[1] + 3 >= right:
        return 0
    return int(rows[coord[0]][coord[1] + 1] == 'M' and rows[coord[0]][coord[1] + 2] == 'A' and rows[coord[0]][coord[1] + 3] == 'S')

def se_mas(coord):
    if coord[0] + 3 >= bottom or coord[1] + 3 >= right:
        return 0
    return int(rows[coord[0] + 1][coord[1] + 1] == 'M' and rows[coord[0] + 2][coord[1] + 2] == 'A' and rows[coord[0] + 3][coord[1] + 3] == 'S')

def s_mas(coord):
    if coord[0] + 3 >= bottom:
        return 0
    return int(rows[coord[0] + 1][coord[1]] == 'M' and rows[coord[0] + 2][coord[1]] == 'A' and rows[coord[0] + 3][coord[1]] == 'S')

def sw_mas(coord):
    if coord[0] + 3 >= bottom or coord[1] - 3 < 0:
        return 0
    return int(rows[coord[0] + 1][coord[1] - 1] == 'M' and rows[coord[0] + 2][coord[1] - 2] == 'A' and rows[coord[0] + 3][coord[1] - 3] == 'S')

def w_mas(coord):
    if coord[1] - 3 < 0:
        return 0
    return int(rows[coord[0]][coord[1] - 1] == 'M' and rows[coord[0]][coord[1] - 2] == 'A' and rows[coord[0]][coord[1] - 3] == 'S')


def count_mas(coord):
    return nw_mas(coord) + n_mas(coord) + ne_mas(coord) + e_mas(coord) + se_mas(coord) + s_mas(coord) + sw_mas(coord) + w_mas(coord)

total = 0
for i, row in enumerate(rows):
    for j, letter in enumerate(row):
        if letter == 'X':
            total += count_mas((i,j))
            

print(total)