
def get_neighbours(i, j, rows, cols):
    neighbours = list()
    for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        rr = i + x
        cc = j + y 
        if not ((0 <= rr and rr < rows) and (0 <= cc and cc < cols)):
            continue
        neighbours.append((rr, cc))
    return neighbours

def update(grid, times, rows, cols):
    step = 0
    grid[0][0] = 1
    grid[0][cols-1] = 1
    grid[rows-1][0] = 1
    grid[rows-1][cols-1] = 1
    while step < times:
        to_on = list()
        to_off = list()
        for i in range(rows):
            for j in range(cols):
                neighbours = get_neighbours(i, j, rows, cols)
                lights_on = 0
                for x, y in neighbours:
                    if grid[x][y] == 1:
                        lights_on += 1
                if (grid[i][j] == 1) and (lights_on != 2 and lights_on != 3):
                    to_off.append((i, j))
                if (grid[i][j] == 0) and lights_on == 3 :
                    to_on.append((i, j))
        for (x, y) in to_on:
            grid[x][y] = 1
        for (x, y) in to_off:
            grid[x][y] = 0
        step += 1
        grid[0][0] = 1
        grid[0][cols-1] = 1
        grid[rows-1][0] = 1
        grid[rows-1][cols-1] = 1

    return grid

def solution(fname):
    rows, cols = 100, 100
    grid = [[0 for _ in range(rows)] for _ in range(cols)]
    with open(fname) as f:
        content = f.read().splitlines()
    i = 0
    j = 0
    for line in content:
        j = 0
        for char in line:
            if char == "#":
                grid[i][j] = 1
            j += 1
        i += 1
    new_grid = update(grid, 100, rows, cols)
    on = 0
    for row in new_grid:
        for val in row:
            if val == 1:
                on += 1
    return on

if __name__ == "__main__":
    print(solution("input.txt"))
