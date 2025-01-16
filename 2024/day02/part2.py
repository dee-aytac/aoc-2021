def is_report_safe(level):
    tolerated = False
    idx = 1
    direction = sum([level[idx + 1] - level[idx] for idx in range(0, len(level) - 1)])
    valid_range = range(1, 4)
    if direction < 0:
        valid_range = range(-3, 0)
    while idx < len(level):
        if (level[idx] - level[idx - 1]) not in valid_range:
            if tolerated:
                return False
            idx = 1
            level.pop(idx)
            tolerated = True
        idx += 1

    return True
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    safe_level_count = 0
    for line in content:
        levels = list(map(int, line.split(' ')))
        if is_report_safe(levels):
            safe_level_count += 1
    return safe_level_count

if __name__ == "__main__":
    print(solution('input.txt')) 
