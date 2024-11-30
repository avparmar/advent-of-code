from util.input_tools import get_input_rows

rows = get_input_rows()

for row in rows:
    items = row.split("\t")
    print(items)