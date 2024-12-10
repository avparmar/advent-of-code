class InTool:
    def __init__(self, filename = "input.txt"):
        with open(filename) as input:
            self.rows = [x for x in input.read().strip().split("\n")]
            input.close()
            
        self.bottom = len(self.rows)
        self.right = len(self.rows[0])
        
    def get_rows(self):
        return self.rows        
    
    def get_bottom(self):
        return self.bottom
    
    def get_right(self):
        return self.right
    
    def get_int_grid(self, sep = None, digit = False):
        if digit:
            return [[int(item) for item in row] for row in self.rows]

        return [[int(item) for item in row.split(sep)] for row in self.rows]
    
    def get_int_row(self, row: str, sep = None, digit = False):
        if digit:
            return [int(item) for item in row]

        return [int(item) for item in row.split(sep)]
    
    def get_first_row(self):
        return self.rows[0]
    
    def get_first_int_row(self, sep = None, digit = False):
        if digit:
            return [int(item) for item in self.rows[0]]
        return [int(item) for item in self.rows[0].split(sep)]
    
    def inbounds(self, coord: tuple[int, int]):
        return 0 <= coord[0] < self.bottom and 0 <= coord[1] < self.right

    def inbounds(self, c1: int, c2: int):
        return 0 <= c1 < self.bottom and 0 <= c2 < self.right
    
    def get_adjacent(self, c1: int, c2: int, diagonals = False):
        res = []
        if self.inbounds(c1 - 1, c2):
            res.append((c1 - 1, c2))
        if self.inbounds(c1 + 1, c2):
            res.append((c1 + 1, c2))
        if self.inbounds(c1, c2 - 1):
            res.append((c1, c2 - 1))
        if self.inbounds(c1, c2 + 1):
            res.append((c1, c2 + 1))
        if diagonals:
            if self.inbounds(c1 - 1, c2 - 1):
                res.append((c1 - 1, c2 - 1))
            if self.inbounds(c1 + 1, c2 + 1):
                res.append((c1 + 1, c2 + 1))
            if self.inbounds(c1 - 1, c2 + 1):
                res.append((c1 - 1, c2 + 1))
            if self.inbounds(c1 + 1, c2 - 1):
                res.append((c1 + 1, c2 - 1))
        return res

def get_input_rows(filename = "input.txt"):
    with open(filename) as input:
        rows = [x for x in input.read().strip().split("\n")]
        input.close()
        
    return rows

def get_int_row(row: str, sep = None):
    return [int(item) for item in row.split(sep)]