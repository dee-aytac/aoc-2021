
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    area_map = list()
    for line in content:
        to_add = [1 if square == "#" else 0 for square in line]
        area_map.append(to_add)
    x, y = 0, 0
    trees = 0
    while True:
        if x == len(area_map) - 1:
            return trees
        if area_map[x % len(area_map)][y % len(area_map[0])]:
            trees += 1
        y += 3
        x += 1

if __name__ == "__main__":
    print(solution('input.txt')) 