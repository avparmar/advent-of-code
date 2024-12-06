from advent_of_code.util.input_tools import get_input_rows, get_int_row

rows = get_input_rows()

rules = set()
rules_done = False
total = 0

def eval_order(row: str):
    ordering = get_int_row(row, ',')
    for i in range(len(ordering)):
        for j in range(i + 1, len(ordering)):
            if f'{ordering[j]}|{ordering[i]}' in rules:
                return 0
    return ordering[len(ordering) // 2]

for row in rows:
    if row == "":
        rules_done = True
        continue
    if not rules_done:
        rules.add(row)
    else:
        total += eval_order(row)
        
print(total)
        