from advent_of_code.util.input_tools import get_input_rows

rows = get_input_rows()

list1 = []
list2 = []
for row in rows:
    items = row.split()
    list1.append(int(items[0]))
    list2.append(int(items[1]))
    
list1.sort()
list2.sort()

sum = 0
for ind in range(len(list1)):
    sum += abs(list1[ind] - list2[ind])
    
print(sum)