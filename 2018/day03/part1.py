
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in content:
        rect_id, _, pos, dim = line.split(' ')
        rect_id = rect_id[1:]
        x_pos, y_pos = pos.split(',')
        y_pos = y_pos[:-1]
        x_pos, y_pos = int(x_pos), int(y_pos)
        width, height = dim.split('x')
        width, height = int(width), int(height)
        for x in range(width):
            for y in range(height):
                grid[x+x_pos][y+y_pos] += 1
    answer = 0
    for row in grid:
        for val in row:
            if val >= 2:
                answer += 1
    return answer

if __name__ == "__main__":
    print(solution('input.txt'))