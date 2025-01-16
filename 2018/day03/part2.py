
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    overlaps = set()
    for line in content:
        rect_id, _, pos, dim = line.split(' ')
        rect_id = int(rect_id[1:])
        x_pos, y_pos = pos.split(',')
        y_pos = y_pos[:-1]
        x_pos, y_pos = int(x_pos), int(y_pos)
        width, height = dim.split('x')
        width, height = int(width), int(height)
        for x in range(width):
            for y in range(height):
                if grid[x+x_pos][y+y_pos] != 0:
                    overlaps.add(grid[x+x_pos][y+y_pos])
                    overlaps.add(rect_id)
                grid[x+x_pos][y+y_pos] = rect_id
        max_id = rect_id
    for idx in range(1, max_id + 1):
        if idx not in overlaps:
            return idx
    print(overlaps)

if __name__ == "__main__":
    print(solution('input.txt'))