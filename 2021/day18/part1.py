grid = []
for line in open('sample.txt'):
    grid.append(line.strip())
for row in grid:
    print(row)
print("*-*")
print(grid[0])
