import math
from collections import defaultdict

def get_info(content):
    max_row = 0
    max_col = 0
    centers = set()
    for line in content:
        num1, num2 = line.split(', ')
        centers.add((int(num1), int(num2)))
        if int(num1) > max_row:
            max_row = int(num1)
        if int(num2) > max_col:
            max_col = int(num2)
    return centers, (max_row, max_col)

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    centers, length = get_info(content)
    all_clusters = dict()
    for (center_x, center_y) in centers:
        all_clusters[(center_x, center_y)] = 0 
    coord_id_to_point = {coord_id: point for coord_id, point in enumerate(centers, start = 1)}
    region_sizes = defaultdict(int)
    infinite_ids = set()

    for i in range(length[0] + 1):
        for j in range(length[1] + 1):
            min_dists = sorted([(abs(r - i) + abs(c - j), coord_id) for coord_id, (r, c) in coord_id_to_point.items()])

            if len(min_dists) == 1 or min_dists[0][0] != min_dists[1][0]:
                coord_id = min_dists[0][1]
                region_sizes[coord_id] += 1

                if i == 0 or i == length[0] or j == 0 or j == length[1]:
                    infinite_ids.add(coord_id)

    return max(size for coord_id, size in region_sizes.items() if coord_id not in infinite_ids)

if __name__ == "__main__":
    print(solution('input.txt')) 

