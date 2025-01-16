
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    contain_other = 0
    for line in content:
        p1, p2 = line.split(',')
        r1_start, r1_end = p1.split('-')
        r2_start, r2_end = p2.split('-')
        l1 = list(range(int(r1_start), int(r1_end) + 1))
        l2 = list(range(int(r2_start), int(r2_end) + 1))
        if all(i in l2 for i in l1) or all(i in l1 for i in l2):
            contain_other += 1
    return contain_other
if __name__ == "__main__":
    print(solution('input.txt')) 
