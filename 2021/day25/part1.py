from copy import deepcopy
grid = list()

for line in open('input.txt'):
    row = list()
    for char in line.strip():
        row.append(char)
    grid.append(row)

rows = len(grid)
cols = len(grid[0])

def advance(grid):
    steps = 0
    not_moved = False
    while not not_moved:
        original_grid = deepcopy(grid)
        not_moved = True
        for i, row in enumerate(original_grid):
            for j, col in enumerate(row):
                if original_grid[i][j] == ">":
                    if original_grid[i][(j + 1) % cols] == ".":
                        not_moved = False
                        grid[i][(j + 1) % cols] = ">"
                        grid[i][j] = "."
        original_grid = deepcopy(grid)
        for i, row in enumerate(original_grid):
            for j, col in enumerate(row):
                if original_grid[i][j] == "v":
                    if original_grid[(i + 1) % rows][j] == ".":
                        not_moved = False
                        grid[(i + 1) % rows][j] = "v"
                        grid[i][j] = "."
        steps += 1
    return steps



if __name__ == "__main__":
    print(advance(grid))

