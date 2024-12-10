from advent_of_code.util.input_tools import InTool
from collections import defaultdict

it = InTool()

row = it.get_first_int_row(digit=True)
size = it.get_right()

file_sizes = defaultdict(list)
file_ptrs = [0] * 9
right_ptr = size - 1 if size % 2 == 1 else size - 2
right_id = size // 2

for ind in range(right_ptr, -1, -2):
    file_sizes[row[ind]].append(ind)
    right_id -= 1
    
def get_next_file(space: int, left_ptr: int):
    best_ind = -1
    best_val = -1
    for i in range(1, space + 1):
        if file_ptrs[i - 1] >= len(file_sizes[i]):
            continue
        ind = file_sizes[i][file_ptrs[i - 1]]
        if ind > best_ind:
            best_ind = ind
            best_val = i - 1    
    if best_ind <= left_ptr:
        return -1
    
    file_ptrs[best_val] += 1
    return best_ind

replaced = set()
total = 0
left_ptr = 0
left_id = 0
left_pos = 0
while left_ptr < right_ptr:        
    # handle pointer on file
    if left_ptr not in replaced:
        total += sum([left_id * pos for pos in range(left_pos, left_pos + row[left_ptr])])
    left_pos += row[left_ptr]
    left_id += 1
    left_ptr += 1

    # handle pointer on free space
    space = row[left_ptr]
    while space != 0:
        ind = get_next_file(space, left_ptr)
        if ind < 0:
            left_pos += space
            break
        replaced.add(ind)
        id = ind // 2
        size = row[ind]
        total += sum([id * pos for pos in range(left_pos, left_pos + size)])
        left_pos += size
        space -= size
    left_ptr += 1
print(total)