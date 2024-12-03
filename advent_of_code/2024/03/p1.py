from re import findall

with open("input.txt") as input:
    mem = input.read()
    input.close()
    
matches = findall(r'mul\(\d+,\d+\)', mem)

def do_mult(match: str):
    nums = list(map(int,findall(r'\d+', match)))
    return nums[0] * nums[1]

print(sum(do_mult(match) for match in matches))