from advent_of_code.util.input_tools import get_input_rows, get_int_row
import numpy as np

rows = get_input_rows()
#rows = get_input_rows('input2.txt')
origin = np.zeros(2, dtype=int)
vertex = np.full(2, len(rows[0]))

freqs = {}
for i, row in enumerate(rows):
    for j, c in enumerate(row):
        if c == '.':
            continue
        if c not in freqs:
            freqs[c] = []
        freqs[c].append(np.array((i,j)))

def inbounds(coord):
    return np.greater_equal(coord, origin).all() and np.less(coord, vertex).all()

antinodes = set()
for letter in freqs:
    startInd = 0
    freq = freqs[letter]
    for left_node in freq:
        startInd += 1
        for right_node in freq[startInd:]:
            slope = right_node - left_node
            #debug_str = f'{left_node}, {right_node} {prime_slope}'
            # find left antinodes
            curr_node = np.copy(left_node)
            while inbounds(curr_node):
                #debug_str += f', {curr_node}'
                if str(curr_node) not in antinodes:
                    #debug_str += '+'
                    antinodes.add(str(curr_node))
                curr_node -= slope
            # find right antinodes
            curr_node = np.copy(left_node)
            while inbounds(curr_node):
                #debug_str += f', {curr_node}'
                if str(curr_node) not in antinodes:
                    #debug_str += '+'
                    antinodes.add(str(curr_node))
                curr_node += slope
            #print(debug_str)
                

print(len(antinodes))