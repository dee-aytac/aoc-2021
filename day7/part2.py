from collections import Counter

def get_lowest(num):
    distance = abs(num - common[0])
    fuel = (distance * (distance + 1)) // 2
    return fuel

with open('input.txt', 'r') as f:
    horizontal_positions = f.read().split(',')
    horizontal_positions = [int(i) for i in horizontal_positions]
    c = Counter(horizontal_positions)
    mean_ = c.most_common()
    lowest_sum = float('inf')
    for common in mean_:
        x = sum(map(get_lowest, horizontal_positions))
        lowest_sum = min(x, lowest_sum)
print(lowest_sum)
