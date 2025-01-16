import array as arr

depth = arr.array('i')
with open('input.txt', 'r') as f:
    for measurement in f:
        depth.append(int(measurement))
depth_increase = 0
prev = float('inf')
for i in range(0, len(depth) - 2):
    new_sum = depth[i] + depth[i + 1] + depth[i + 2]
    if new_sum > prev:
        depth_increase += 1
    prev = new_sum
print(depth_increase)