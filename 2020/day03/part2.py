from functools import reduce

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    area_map = list()
    for line in content:
        to_add = [1 if square == "#" else 0 for square in line]
        area_map.append(to_add)
    x, y = 0, 0
    all_trees = list()
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for y_slope, x_slope in slopes:
        trees = 0
        x = 0
        y = 0
        while True:
            if x == len(area_map) - 1:
                all_trees.append(trees)
                break
            if area_map[x % len(area_map)][y % len(area_map[0])]:
                trees += 1
            y += y_slope
            x += x_slope

    return reduce(lambda x, y: x * y, all_trees)
    

if __name__ == "__main__":
    print(solution('input.txt')) 
