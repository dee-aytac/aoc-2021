with open('input.txt', 'r') as f:
    grid = []
    risk_level = 0
    for readline in f:
        line = readline.strip()
        row = [int(i) for i in line]
        grid.append(row)

rows = len(grid)
cols = len(grid[0])
low_points = []
for r in range(rows):
    for c in range(cols):
        lower = True
        for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            rr = r + x
            cc = c + y
            
            if not ((0 <= rr and rr < rows) and (0 <= cc and cc < cols)):
                continue

            if grid[rr][cc] <= grid[r][c]:
                lower = False
                break 
        if lower:
            low_points.append((r, c))


basin_lengths = []
for r, c in low_points:
    stack = [(r, c)]
    visited_cells = set()
    num = 0
    while len(stack) > 0:
        r, c = stack.pop()
        if (r, c) in visited_cells:
            continue
        else:
            num += 1
        visited_cells.add((r, c))

        for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            rr = r + x
            cc = c + y
            
            if not ((0 <= rr and rr < rows) and (0 <= cc and cc < cols)):
                continue

            if grid[rr][cc] == 9:
                continue
            stack.append((rr, cc))

    basin_lengths.append(num)
    
basin_lengths = sorted(basin_lengths, reverse = True)
print(basin_lengths[0] * basin_lengths[1] * basin_lengths[2])

