from advent_of_code.util.input_tools import InTool

it = InTool('input.txt')

robots = []
width = 101
height = 103
v_median = width // 2
h_median = height // 2

for row in it.rows:
    row_words = row.split(' ')
    p = row_words[0][2:].split(',')
    p_x = int(p[0])
    p_y = int(p[1])
    v = row_words[1][2:].split(',')
    v_x = int(v[0])
    v_y = int(v[1])
    robots.append([p_x, p_y, v_x, v_y])
    
seconds = 500

for robot in robots:
    robot[0] = (robot[0] + (robot[2] * seconds)) % width
    robot[1] = (robot[1] + (robot[3] * seconds)) % height


# NW, NE, SW, SE
safeties = [0, 0, 0, 0]

for robot in robots:    
    if robot[0] == v_median or robot[1] == h_median:
        continue
    
    quadrant = 0
    if robot[1] > h_median:
        quadrant += 2
    if robot[0] > v_median:
        quadrant += 1
    
    safeties[quadrant] += 1

factor = 1
for item in safeties:
    factor *= item

print(factor)