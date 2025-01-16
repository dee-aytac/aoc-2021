
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    grid = list()
    for line in content:
        grid.append([int(char) for char in line])
    visibles = set()
    for idx_r in range(len(grid)):
        for idx_c in range(len(grid[0])):
            height = grid[idx_r][idx_c]
            if idx_r == 0 or idx_c == 0 or idx_r == len(grid) - 1 or idx_c == len(grid[0]) - 1:
                visibles.add((idx_r, idx_c))
                continue

            for x_step, y_step in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                block_x = idx_r
                block_y = idx_c
                visible = True
                while True:
                    block_x += x_step
                    block_y += y_step
                    if block_x < 0 or block_x >= len(grid) or block_y < 0 or block_y >= len(grid[0]):
                        break
                    if grid[block_x][block_y] >= height:
                        visible = False
                        break
                if visible:
                    visibles.add((idx_r, idx_c))

    return len(visibles)

if __name__ == "__main__":
    print(solution('input.txt')) 
