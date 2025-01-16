def is_report_safe(level):
    for idx in range(1, len(level)):
        diff = abs(level[idx] - level[idx - 1])
        if not(diff >= 1 and diff <= 3):
            return False
    if level == sorted(level) or level == sorted(level, reverse=True):
        return True
    return False

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    safe_level_count = 0
    for line in content:
        levels = list(map(int, line.split(' ')))
        if is_report_safe(levels):
            safe_level_count += 1
            print(levels)
    return safe_level_count
if __name__ == "__main__":
    print(solution('input.txt')) 
