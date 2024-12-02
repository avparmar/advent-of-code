from advent_of_code.util.input_tools import get_input_rows, get_int_row

#rows = get_input_rows("alt_in.txt")
rows = get_input_rows()

def process_report(report: list[int], ignore = None):
    if ignore != None:
        #print("<-- ",report," -->, ",ignore)
        pass
    bad = -1
    is_inc = -1
    prev = -1
    for ind in range(0,len(report)):
        if ignore == ind:
            continue
        curr = report[ind]
        if prev == -1:
            prev = curr
            continue
        if prev == curr:
            bad = ind
            break
        if is_inc == -1:
            #print(prev, curr)
            is_inc = int(prev < curr)
        if ignore != None:
           #print(prev,curr)
           pass
        if is_inc == 1 and prev > curr or prev + 3 < curr:
            bad = ind
            break
        if is_inc == 0 and prev < curr or prev - 3 > curr:
            bad = ind
            break
        prev = curr
    
    rv = 0
    if bad != -1 and ignore != None:
        rv = 0
    elif bad != -1 and ignore == None:
        #print(bad - 1, bad, bad + 1)
        rv = max(process_report(report, bad),process_report(report, bad - 1),process_report(report, bad - 2))
    else:
        rv = 1
    if rv == 0:
        #print("BAD ROW: ", report, ignore, is_inc, bad)
        pass
    if rv == 1:
        #print("GOOD ROW: ", report, ignore, is_inc)
        pass
    return rv

safe_rows = 0
for row in rows:
    report = get_int_row(row)
    
    safe_rows += process_report(report)

print(safe_rows)