with open('sample.txt') as f:
    p1, p2 = f.read().strip().split('\n')
    p1 = int(p1[-1])
    p2 = int(p2[-1])