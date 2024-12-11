from advent_of_code.util.input_tools import InTool

it = InTool('input3.txt')

# number of stones after i generations, starting at 0
# 0, 1, 2024, 20 24, 2 0 2 4
zero_gen_lens = [1, 1, 1, 2, 4]

# same for 2
# 2, 4048, 40 48, 4 0 4 8
two_gen_lens = [1, 1, 2, 4]

[[# 0
    '0', '1', '2024', '20 24', '2 0 2 4',
],
 [# 2
     '2', '4048', '40 48', '4 0 4 8',
 ],
 [# 3
     '3', '6072', '60 72', '6 0 7 2',
 ],
 [# 4
     '4', '4096', '40 96', '4 0 9 6',
 ],
 [# 5
     '5', '10120', '20482880', '2048 2880', '20 48 28 80', '2 0 4 8 2 8 8 0',
 ],
 [#6
    '6', '12144', '24579456', '2457 9456', '24 57 94 56', '2 4 5 7 9 4 5 6', 
 ],
 [#7
    '7',  
 ]
 ]

zero_gens = {}    
stones = it.get_first_row()
count = 1
for i in range(9):
    zero_gens[8 - i] = 0
    new_stones = ''
    for stone in stones.split(' '):
        if len(stone) == 0:
            continue
        if stone == '0':
            zero_gens[9 - i] += 1
            #print(stone, ' 1')
        elif stone == '1':
            zero_gens[8 - i] += 1
        elif len(stone) % 2 == 0:
            half = len(stone) // 2
            new_stones += f' {stone[0:half]} {int(stone[half:])}'
            count += 1
            #print(stone, f' {stone[0:half]} {int(stone[half:])}')
        else:
            i_stone = int(stone)
            #new_stones += f' {(i_stone << 11) - ((i_stone << 4) + (i_stone << 3))}'
            new_stones += f' {i_stone * 2024}'
            #print(stone, f' {i_stone * 2024}')
    stones = new_stones
    print(f'after blink {i + 1}: {count}, {zero_gens}')
    print(stones)

print(len(stones.strip().split(' ')))