def solution(fname):
    with open(fname, 'r') as f:
        content = sorted(f.read().strip().split('\n'))
    
    black_list = list()

    for line in content:
        low, high = line.split('-')
        black_list.append((int(low), int(high)))
    idx = 0
    ip = 0
    black_list.sort()
    total_ip = 0
    while ip <= 2 ** 32:
        valid = True
        if idx == len(black_list):
            break
        low, high = black_list[idx]
        if ip >= low and ip >= high:
            idx += 1
            continue
        if low <= ip <= high:
            valid = False
        if valid:
            total_ip += 1
            ip = high + 1
        else:
            idx += 1
            ip = high + 1

    return total_ip

if __name__ == "__main__":
    print(solution('input.txt'))