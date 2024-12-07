from advent_of_code.util.input_tools import get_input_rows, get_int_row
from collections import deque

rows = get_input_rows()

total = 0
for row in rows:
    itemized = row.split()
    target = int(itemized[0][:-1])
    rhs = [int(item) for item in itemized[2:]]
    curr_sums = deque([int(itemized[1])])
    last_digit = len(rhs) - 1
    for ind, num in enumerate(rhs):
        iter_count = len(curr_sums)
        for _ in range(iter_count):
            curr_sum = curr_sums.pop()
            add_res = curr_sum + num
            mul_res = curr_sum * num
            if ind == last_digit:
                if add_res == target or mul_res == target:
                    total += target
                    break
            else:
                if add_res <= target:
                    curr_sums.appendleft(add_res)
                if mul_res <= target:
                    curr_sums.appendleft(mul_res)

print(total)