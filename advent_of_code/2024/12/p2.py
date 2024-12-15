from advent_of_code.util.input_tools import InTool

it = InTool('input.txt')

# count perimeter, save in grid
perimeters = []

for i in range(it.bottom):
    perimeters.append([0] * it.right)

for i in range(it.bottom):
    for j in range(it.right):
        cell = it.rows[i][j]
        delta = 0
        # north side
        if it.get_or_default(i - 1, j) != cell and (it.get_or_default(i, j + 1) != cell or it.get_or_default(i - 1, j + 1) == cell):
            delta += 1
        # east side
        if it.get_or_default(i, j + 1) != cell and (it.get_or_default(i + 1, j) != cell or it.get_or_default(i + 1, j + 1) == cell):
            delta += 1
        # west side
        if it.get_or_default(i, j - 1) != cell and (it.get_or_default(i - 1, j) != cell or it.get_or_default(i - 1, j - 1) == cell):
            delta += 1
        # south side
        if it.get_or_default(i + 1, j) != cell and (it.get_or_default(i, j - 1) != cell or it.get_or_default(i + 1, j - 1) == cell):
            delta += 1
        perimeters[i][j] = delta
            
                

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

#for perimeter in perimeters:
 #   print(perimeter)

print(sum(region[0] * region[1] for region in regions))
    
        
        