from advent_of_code.util.input_tools import get_input_rows, get_int_row

rows = get_input_rows()

safe_rows = 0
for row in rows:
    report = get_int_row(row)

    if report[0] == report[1]:
        continue

    prev = report[0]
    is_inc = report[0] < report[1]
    
    safe_rows += 1
    for ind in range(1,len(report)):
        curr = report[ind]
        if prev == curr:
            safe_rows -= 1
            break
        if is_inc and prev > curr or prev + 3 < curr:
            safe_rows -= 1
            break
        if not is_inc and prev < curr or prev - 3 > curr:
            safe_rows -= 1
            break
        prev = curr

print(safe_rows)