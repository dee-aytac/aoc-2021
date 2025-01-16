
def get_info(content):
    max_row = 0
    max_col = 0
    centers = list()
    for line in content:
        num1, num2 = line.split(', ')
        centers.append([int(num1), int(num2)])
        if int(num1) > max_row:
            max_row = int(num1)
        if int(num2) > max_col:
            max_col = int(num2)
    return centers, (max_row, max_col)


def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    centers, length = get_info(content)
    region = 0
    limit = 10000
    for pos_x in range(length[0] + 1):
        for pos_y in range(length[1] + 1):
            region += int(sum(abs(center_x - pos_x) + abs(center_y - pos_y) for center_x, center_y in centers) < limit)
    return region

if __name__ == "__main__":
    print(solution('input.txt')) 

