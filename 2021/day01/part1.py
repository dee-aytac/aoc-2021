import array as arr

depth = arr.array('i')
with open('input.txt', 'r') as f:
    for measurement in f:
        depth.append(int(measurement))
depth_increase = 0
for i in range(0, len(depth) - 1):
    if depth[i + 1] > depth[i]:
        depth_increase += 1
print(depth_increase)