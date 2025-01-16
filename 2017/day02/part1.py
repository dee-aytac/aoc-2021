def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    checksum = 0
    for idx, line in enumerate(content):
        row = line.split('\t')
        row_min = float("inf")
        row_max = float("-inf")
        for num in row:
            row_min = min(row_min, int(num))
            row_max = max(row_max, int(num))
        checksum += row_max - row_min
    return checksum

if __name__ == "__main__":
    print(solution('input.txt'))