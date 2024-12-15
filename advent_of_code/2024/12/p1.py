from advent_of_code.util.input_tools import InTool

it = InTool('input.txt')

# count perimeter, save in grid
perimeters = []

for i in range(it.bottom):
    if i == 0 or i == it.bottom - 1:
        perimeters.append([2] + [1] * (it.right - 2) + [2])
    else:
        perimeters.append([1] + [0] * (it.right - 2) + [1])

for i in range(it.bottom):
    for j in range(it.right):
        cell = it.rows[i][j]
        if j != it.right - 1 and cell != it.rows[i][j + 1]:
            perimeters[i][j] += 1
            perimeters[i][j + 1] += 1
        if i != it.bottom - 1 and cell != it.rows[i + 1][j]:
            perimeters[i][j] += 1
            perimeters[i + 1][j] += 1

# count regions by dfs exploring.   
regions = []
next_region = 0
explored = set()

def explore(plant: str, region: int, i: int, j: int):
    if (i << 8) + j in explored or not it.inbounds(i, j) or it.rows[i][j] != plant:
        return
    
    regions[region][0] += perimeters[i][j]
    regions[region][1] += 1
    explored.add((i << 8) + j)
    explore(plant, region, i + 1, j)
    explore(plant, region, i - 1, j)
    explore(plant, region, i, j + 1)
    explore(plant, region, i, j - 1)

for i in range(it.bottom):
    for j in range(it.right):
        if (i << 8) + j not in explored:
            regions.append([0, 0])
            explore(it.rows[i][j], next_region, i, j)
            next_region += 1

print(sum(region[0] * region[1] for region in regions))
    
        
        