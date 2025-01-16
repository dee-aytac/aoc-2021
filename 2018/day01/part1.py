
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    total_sum = 0
    for line in content:
        total_sum += int(line)
    return total_sum

if __name__ == "__main__":
    print(solution('input.txt'))