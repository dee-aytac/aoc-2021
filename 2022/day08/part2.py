
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    grid = list()
    for line in content:
        grid.append([int(char) for char in line])
    max_scenic_score = float("-inf")
    for idx_r in range(len(grid)):
        for idx_c in range(len(grid[0])):
            height = grid[idx_r][idx_c]
            scenic_score = 1
            for x_step, y_step in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                trees_seen = 0
                block_x = idx_r
                block_y = idx_c
                visible = True
                while True:
                    block_x += x_step
                    block_y += y_step
                    if block_x < 0 or block_x >= len(grid) or block_y < 0 or block_y >= len(grid[0]):
                        scenic_score *= trees_seen
                        break
                    if grid[block_x][block_y] >= height:
                        trees_seen += 1
                        scenic_score *= trees_seen
                        break
                    else:
                        trees_seen += 1
            max_scenic_score = max(scenic_score, max_scenic_score)
    return max_scenic_score

if __name__ == "__main__":
    print(solution('input.txt')) 
