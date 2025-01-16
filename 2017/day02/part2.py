def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    checksum = 0
    for idx, line in enumerate(content):
        row = [int(n) for n in line.split('\t')]
        row.sort()
        for i, divisor in enumerate(row):
            for j in range(i + 1, len(row)):
                if (row[j] / divisor).is_integer():
                    print(row[j] / divisor)
                    checksum += row[j] / divisor
    return checksum

if __name__ == "__main__":
    print(solution('input.txt'))