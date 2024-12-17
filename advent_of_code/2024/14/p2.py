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
    
def visualize():
    locs = set()
    for robot in robots:
        locs.add(f'{robot[0]},{robot[1]}')
    
    for i in range(height):
        row_str = ''
        for j in range(width):
            if f'{j},{i}' not in locs:
                row_str += '.'
            else:
                row_str += '*'
        print(row_str)

skip = 6000    
seconds = 3000


for robot in robots:
    robot[0] = (robot[0] + (robot[2] * skip)) % width
    robot[1] = (robot[1] + (robot[3] * skip)) % height

second = 0
while second < seconds:
    locs = set()
    for robot in robots:
        robot[0] = (robot[2] + robot[0]) % width
        robot[1] = (robot[3] + robot[1]) % height
        locs.add((robot[0], robot[1]))
    
    for i in range(height):
        if second > seconds:
            break
        for j in range(width):
            if (j, i) in locs and (j + 1, i) in locs and (j + 2, i) in locs and (j + 3, i) in locs and (j + 4, i) in locs and (j + 5, i) in locs and (j + 6, i) in locs and (j + 7, i) in locs:             
                visualize()
                print(f't = {skip + second + 1}')
                second = seconds + 1
                break
    second += 1
