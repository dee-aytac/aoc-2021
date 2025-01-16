
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')[0]
    total_sum = 0
    length = len(content)
    for idx, char in enumerate(content):
        next_char = content[(idx+1)%length]
        if char == next_char:
            total_sum += int(next_char)

    return total_sum

if __name__ == "__main__":
    print(solution('input.txt'))