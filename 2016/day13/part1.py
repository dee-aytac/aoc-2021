from collections import deque

def print_map(grid):
    print(" ", end=" ")
    for i in range(len(grid)):
        print(i, end="")
    print()
    print("  ", end="")
    for idx_row, row in enumerate(grid):
        for idx_col, col in enumerate(row):
            if col == 1:
                print("#", end="")
            else:
                print(".", end="")
        print("")
        print(f"{idx_row} ", end="")

def solution(favorite_number, goal_x, goal_y):
    map_size = 50
    grid = [[0 for _ in range (map_size)] for _ in range(map_size)]
    for i in range(map_size):
        for j in range(map_size):
            result = (j*j + 3*j + 2*i*j + i + i*i) + favorite_number
            ones = 0
            for char in str(bin(result)):
                if char == "1":
                    ones += 1
            if ones % 2 != 0:
                grid[i][j] = 1
    
    visited = set()
    steps = 0
    deq = deque()
    start_x, start_y = 1, 1
    deq.append((start_x, start_y, 0))
    visited.add((start_x, start_y))
    while True:
        pos = deq.popleft()
        current_x, current_y, steps = pos[0], pos[1], pos[2]
        if current_x == goal_x and current_y == goal_y:
            return steps
        for direction in [1, -1]:
            current_x += direction
            if (current_x, current_y) not in visited and grid[current_y][current_x] == 0:
                deq.append((current_x, current_y, steps + 1))
                visited.add((current_x, current_y))
            current_x = pos[0]

        for direction in [1, -1]:
            current_y += direction
            if (current_x, current_y) not in visited and grid[current_y][current_x] == 0:
                deq.append((current_x, current_y, steps + 1))
                visited.add((current_x, current_y))
            current_y = pos[1]
if __name__ == "__main__":
    print(solution(1362, 31, 39))