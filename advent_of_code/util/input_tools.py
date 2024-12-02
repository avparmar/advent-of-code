def get_input_rows(filename = "input.txt"):
    with open(filename) as input:
        rows = [x for x in input.read().strip().split("\n")]
        input.close()
        
    return rows

def get_int_row(row: str, sep = None):
    return list(map(int, row.split(sep)))