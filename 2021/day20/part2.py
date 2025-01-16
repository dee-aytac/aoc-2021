with open('input.txt') as f:
    data = f.read().strip().split("\n")
encode = data[0]
initial = data[2:]

grid = set()

for idx_x, row in enumerate(initial):
    for idx_y, col in enumerate(row):
        if initial[idx_x][idx_y] == "#":
            grid.add((idx_x, idx_y))

def get_dim(grid):
    min_row, max_row = float('inf'), float('-inf')
    min_col, max_col = float('inf'), float('-inf')
    for row, col in grid:
        min_row, max_row = min(min_row, row), max(max_row, row)
        min_col, max_col = min(min_col, col), max(max_col, col)
    return min_row, max_row, min_col, max_col


mnr, mxr, mnc, mxc = get_dim(grid)
mnr -= 200
mxr += 200
mnc -= 200
mxc += 200
for _ in range(50):
    new = set()
    for row in range(mnr, mxr + 1):
        for col in range(mnc, mxc + 1):
            s = ""
            for (r, c) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
                rr = row + r 
                cc = col + c
                s += "1" if (rr, cc) in grid else "0"
            index = int(s, 2)
            new_char = encode[index]
            if new_char == "#":
                #print("Added", (row, col))

                new.add((row, col))
    
    grid = new
    mnr += 3
    mxr -= 3
    mnc += 3
    mxc -= 3

print(len(grid))