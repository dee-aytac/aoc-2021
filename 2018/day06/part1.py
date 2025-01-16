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
    clusters = defaultdict(int)
    infinites = set()

    for pos_x in range(length[0] + 1):
        for pos_y in range(length[1] + 1):
            min_dists = [(abs(center_x - pos_x) + abs(center_y - pos_y), coord_id) for coord_id, (center_x, center_y) in coord_id_to_point.items()]
            min_dists = sorted(min_dists)
            if min_dists[0][0] != min_dists[1][0]:
                coord_id = min_dists[0][1]
                clusters[coord_id] += 1

                if pos_x == 0 or pos_x == length[0] or pos_y == 0 or pos_y == length[1]:
                    infinites.add(coord_id)

    return max(size for coord_id, size in clusters.items() if coord_id not in infinites)

if __name__ == "__main__":
    print(solution('input.txt')) 

