with open('input.txt') as input:
    target = int(input.read())
    input.close()

layer_max = 1
layer = 0

while (layer_max < target):
    layer += 1
    layer_max += 8 * layer
    
# the number right before the start of this layer
layer_prev = layer_max - (layer * 8)
layer_size = layer * 8

# get target position on layer
target_pos = (target - layer_prev) % layer_size

# get target distance to center of row/col
target_offset = target
for i in range(4):
    target_offset = min(abs(target_pos - (layer + (layer * 2) * i)), target_offset)

print(layer + target_offset)

# 1,3,5,7
# 2,6,10,14
# 3,9,15,21