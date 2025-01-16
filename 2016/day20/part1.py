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
    while True:
        valid = True
        low, high = black_list[idx]
        if ip >= low and ip >= high:
            idx += 1
            continue
        if low <= ip <= high:
            valid = False
        if valid:
            return ip
        else:
            idx += 1
            ip = high + 1
            
    return ip
    
if __name__ == "__main__":
    print(solution('input.txt'))