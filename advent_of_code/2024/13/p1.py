from advent_of_code.util.input_tools import InTool
from re import findall

it = InTool('input.txt')

total = 0
for i in range(0, it.bottom, 4):
    x_1 = int(it.rows[i][12:14])
    y_1 = int(it.rows[i][18:20])
    x_2 = int(it.rows[i + 1][12:14])
    y_2 = int(it.rows[i + 1][18:20])

    prize_re = findall(r'\d+', it.rows[i + 2])
    c_1 = int(prize_re[0]) * -1
    c_2 = int(prize_re[1]) * -1
    
    x_num = ((x_2 * c_2) - (y_2 * c_1))
    y_num = ((y_1 * c_1) - (x_1 * c_2))
    denom = ((y_2 * x_1) - (y_1 * x_2))
    if x_num % denom == 0 and y_num % denom == 0:
        total += 3 * (x_num // denom) + (y_num // denom)
print(total)