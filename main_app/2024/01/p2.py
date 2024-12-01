from main_app.util.input_tools import get_input_rows

rows = get_input_rows()

list1 = []
list2 = []
for row in rows:
    items = row.split()
    list1.append(int(items[0]))
    list2.append(int(items[1]))
    
list1.sort()
list2.sort()

score = 0
list1_counts = {}
list2_counts = {}

for loc in list1:
    if not loc in list1_counts:
        list1_counts[loc] = 1
    else:
        list1_counts[loc] += 1
for loc in list2:
    if not loc in list2_counts:
        list2_counts[loc] = 1
    else:
        list2_counts[loc] += 1
        
for loc in list1_counts:
    if loc in list2_counts:
        score += loc * list1_counts[loc] * list2_counts[loc]
    
print(score)