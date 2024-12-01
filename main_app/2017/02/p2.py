from main_app.util.input_tools import get_input_rows

rows = get_input_rows()

sum = 0

for row in rows:
    currSum = sum
    items = [int(item) for item in row.split("\t")]
    for i in range(len(items)):
        for j in range(len(items)):
            if i == j:
                continue
            max_item = max(items[i],items[j])
            min_item = min(items[i],items[j])
            if max_item % min_item == 0:
                sum += max_item // min_item
                break
        if sum > currSum:
            break
    
print(sum)