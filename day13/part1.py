

max_rows = float('-inf')
max_cols = float('-inf')
dots = set()
folds = []
for line in open('input.txt', 'r'):
    if line.strip():
        if line[0] == "f":
            folds.append(line.strip())
        else:
            y, x = line.strip().split(',')
            dots.add((int(x), int(y)))
            max_rows = max(max_rows, int(x))
            max_cols = max(max_cols, int(y))


grid = [[0 for x in range(max_cols + 1)] for y in range(max_rows + 1)]

for x, y in dots:
    grid[x][y] = 1


fold = folds[0]
info = fold.split(' ')[2]
dim, pos = (info.split('='))
pos = int(pos)
if dim == "y":
    for r in range(pos, max_rows + 1):
        for c in range(max_cols + 1):
            if grid[r][c]:
                new_row = r - ((r - pos) * 2)
                grid[new_row][c] = 1
    new_grid = grid[:pos]
    max_cols = pos
elif dim == "x":
    new_grid = [[0 for x in range(pos)] for y in range(max_rows + 1)]
    for r in range(max_rows + 1):
        for c in range(pos, max_cols + 1):

            if grid[r][c]:
                new_col = c - ((c - pos) * 2)
                grid[r][new_col] = 1
    for r in range(max_rows + 1):
        for c in range(pos):
            new_grid[r][c] = grid[r][c]
    max_rows = pos


print(sum(sum(new_grid, [])))