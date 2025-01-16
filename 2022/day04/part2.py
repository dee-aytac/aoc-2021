
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    overlap = 0
    for line in content:
        p1, p2 = line.split(',')
        r1_start, r1_end = p1.split('-')
        r2_start, r2_end = p2.split('-')
        l1 = list(range(int(r1_start), int(r1_end) + 1))
        l2 = list(range(int(r2_start), int(r2_end) + 1))
        if len(set(l1).intersection(set(l2))):
            overlap += 1
    return overlap
if __name__ == "__main__":
    print(solution('input.txt')) 
