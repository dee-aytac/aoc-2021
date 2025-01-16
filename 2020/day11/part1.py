from copy import deepcopy

# # -> occupied | L -> empty | . -> floor
def change_state(grid):
    new_grid = list()
    for idx_r, row in enumerate(grid):
        new_row = list()
        for idx_c, col in enumerate(row):
            neighbours = {"empty": 0, "floor": 0, "occupied": 0}
            for rr in range(-1, 2, 1):
                for cc in range(-1, 2, 1):
                    if rr == 0 and cc == 0:
                        continue
                    if idx_r + rr >= 0 and idx_r + rr < len(grid) and idx_c + cc >= 0 and idx_c + cc < len(grid[0]):
                        if grid[idx_r + rr][idx_c + cc] == ".":
                            neighbours["floor"] += 1
                        elif grid[idx_r + rr][idx_c + cc] == "#":
                            neighbours["occupied"] += 1
                        elif grid[idx_r + rr][idx_c + cc] == "L":
                            neighbours["empty"] += 1
            if col == ".":
                new_row.append(".")
            elif col == "L" and neighbours["occupied"] == 0:
                new_row.append("#")
            elif col == "#" and neighbours["occupied"] >= 4:
                new_row.append("L")
            else:
                new_row.append(grid[idx_r][idx_c])
        new_grid.append(new_row)
    return new_grid, (new_grid != grid)

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    grid = list()
    for line in content:
        grid.append([char for char in line])
    change = True
    while change:
        grid, change = change_state(grid)
    return sum(sum([[1 if val == '#' else 0 for val in row] for row in grid], []))

if __name__ == "__main__":
    print(solution('input.txt')) 
