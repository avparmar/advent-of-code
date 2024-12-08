from advent_of_code.util.input_tools import get_input_rows, get_int_row
import numpy as np

rows = get_input_rows()
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
            # find left antinode
            left_antinode = left_node - slope
            if inbounds(left_antinode) and str(left_antinode) not in antinodes:
                antinodes.add(str(left_antinode))
            # find right antinode
            right_antinode = right_node + slope
            if inbounds(right_antinode) and str(right_antinode) not in antinodes:
                antinodes.add(str(right_antinode)) 

print(len(antinodes))