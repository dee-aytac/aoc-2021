grid = []
for line in open('input.txt', 'r'):
    row = []
    for char in line.strip():
        row.append(int(char))
    grid.append(row)
rows = len(grid)
cols = len(grid[0])

def count_flashes(times):
    flashes = 0
    for _ in range(times):
        flashed = set()
        for row in range(rows):
            for col in range(cols):
                grid[row][col] += 1
        
        while True:
            change = False
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] > 9 and (row, col) not in flashed:
                        flashed.add((row, col))
                        change = True
                        for x, y in [(-1, -1), (1, 1), (1, -1), (-1, 1), (0, 1), (0, -1), (-1, 0), (1, 0)]:
                            rr = row + x
                            cc = col + y        
                            if not ((0 <= rr and rr < rows) and (0 <= cc and cc < cols)):
                                continue
                            grid[rr][cc] += 1
            if change == False:
                break
        flashes += len(flashed)
        for f in flashed:
            r = f[0]
            c = f[1]
            grid[r][c] = 0
    return flashes
print(count_flashes(100))