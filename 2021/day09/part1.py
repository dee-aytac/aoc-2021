with open('input.txt', 'r') as f:
    grid = []
    risk_level = 0
    for readline in f:
        line = readline.strip()
        row = [int(i) for i in line]
        grid.append(row)

rows = len(grid)
cols = len(grid[0])
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
            print(grid[r][c])
            risk_level += grid[r][c] + 1

print(risk_level)

