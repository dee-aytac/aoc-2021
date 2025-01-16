
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    total_sum = 0
    frequency = set()
    frequency.add(0)
    while True:
        for line in content:
            total_sum += int(line)
            if total_sum in frequency:
                return total_sum
            frequency.add(total_sum)
    return -1

if __name__ == "__main__":
    print(solution('input.txt'))