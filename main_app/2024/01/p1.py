from main_app.util.input_tools import get_input_rows

rows = get_input_rows()

list1 = []
list2 = []
for row in rows:
    items = row.split()
    print(items)
    list1.append[int(items[0])]
    list2.append[int(items[1])]
    
print(list1[0:3])
print(list2[0:3])