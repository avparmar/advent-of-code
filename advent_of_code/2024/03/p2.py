from re import findall,split

with open("input.txt") as input:
    mem = ''.join(input.read().strip().split("\n"))
    input.close()
    
doables = split(r'don\'t\(\).*?(do\(\)|\Z)', mem)

def do_mult(match: str):
    nums = list(map(int,findall(r'\d+', match)))
    return nums[0] * nums[1]

def process_doable(doable: str):
    matches = findall(r'mul\(\d+,\d+\)', doable)
    return sum(do_mult(match) for match in matches)

print(sum(process_doable(doable) for doable in doables))