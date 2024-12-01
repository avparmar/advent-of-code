from advent_of_code.util.input_tools import get_input_rows

rows = get_input_rows()

sum = 0

for row in rows:
    items = row.split("\t")
    min = max = int(items[0])
    for item in items:
        int_item = int(item)
        if int_item < min:
            min = int_item
        elif int_item > max:
            max = int_item
    sum += max - min
    
print(sum)