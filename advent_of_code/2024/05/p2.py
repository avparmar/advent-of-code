from advent_of_code.util.input_tools import get_input_rows, get_int_row

rows = get_input_rows()

rules = set()
rules_done = False
total = 0

# it's the item with <len/2 rules to the left and right, respectively
def find_middle_of_shitty_row(ordering):
    limit = len(ordering) // 2
    for page in ordering:
        left_ct = 0
        right_ct = 0
        for other in ordering:
            if page == other:
                continue
            if f'{page}|{other}' in rules:
                right_ct += 1
                if right_ct > limit:
                    break
            if f'{other}|{page}' in rules:
                left_ct += 1
                if left_ct > limit:
                    break
        if left_ct == limit and right_ct == limit:
            return page
    return 0

def eval_order(row: str):
    ordering = get_int_row(row, ',')
    for i in range(len(ordering)):
        for j in range(i + 1, len(ordering)):
            if f'{ordering[j]}|{ordering[i]}' in rules:
                return find_middle_of_shitty_row(ordering)
    return 0

for row in rows:
    if row == "":
        rules_done = True
        continue
    if not rules_done:
        rules.add(row)
    else:
        total += eval_order(row)
        
print(total)
        