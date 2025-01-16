from collections import deque 
from string import ascii_lowercase

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    alphabet = ascii_lowercase
    grid = list()
    for line in content:
        grid.append([char for char in line])
    starting_positions = list()
    for i1, row in enumerate(grid):
        for i2, val in enumerate(row):
            if val == "a" or val == "S":
                starting_positions.append((i1, i2))
    path = deque()
    for x_pos, y_pos in starting_positions:
        visited = set()
        visited.add((x_pos, y_pos))
        path.append([0, x_pos, y_pos, visited, "a", ""])
    while True:
        curr_cost, x_pos, y_pos, visited, curr_elevation, curr_path = path.popleft()
        for x_step, y_step in ([0, 1], [1, 0], [-1, 0], [0, -1]):
            next_x = x_pos + x_step
            next_y = y_pos + y_step
            if next_x >= 0 and next_x < len(grid) and next_y >= 0 and next_y < len(grid[0]):
                next_elevation = grid[next_x][next_y]
                if next_elevation == "E":
                    if alphabet.index(curr_elevation) == alphabet.index("z") - 1:
                        return curr_cost + 1
                    break
                if next_elevation == "S":
                    next_elevation = "a"
                if next_elevation <= curr_elevation or alphabet.index(curr_elevation) + 1 == alphabet.index(next_elevation):
                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        path.append([curr_cost + 1, next_x, next_y, visited, next_elevation, curr_path + next_elevation])

if __name__ == "__main__":
    print(solution('input.txt')) 