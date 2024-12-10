from advent_of_code.util.input_tools import InTool

it = InTool()

row = it.get_first_int_row(digit=True)
size = it.right

left_ptr = 0
left_id = 0
right_ptr = size - 1 if size % 2 == 1 else size - 2
right_id = size // 2
total = 0
left_pos = 0
while left_ptr < right_ptr:
    # handle pointer on file
    total += sum([left_id * pos for pos in range(left_pos, left_pos + row[left_ptr])])
    left_pos += row[left_ptr]
    left_id += 1
    left_ptr += 1

    # handle pointer on free space
    space = row[left_ptr]
    while space != 0 and left_ptr < right_ptr:
        if row[right_ptr] > space:
            total += sum([right_id * pos for pos in range(left_pos, left_pos + space)])
            left_pos += space
            row[right_ptr] -= space
            space = 0
        else:
            total += sum([right_id * pos for pos in range(left_pos, left_pos + row[right_ptr])])
            left_pos += row[right_ptr]
            space -= row[right_ptr]
            right_ptr -= 2
            right_id -= 1
    left_ptr += 1

print(total)

