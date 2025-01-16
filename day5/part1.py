with open('input.txt', 'r') as f:
    content = f.read().split('\n')
    s = set()
    overlaps = set()
    for line in content:
        line = line.split(' -> ')
        x_1 = int(line[0].split(',')[0])
        x_2 = int(line[1].split(',')[0])
        y_1 = int(line[0].split(',')[1])
        y_2 = int(line[1].split(',')[1])
        if x_1 == x_2:
            bigger = max(y_1, y_2)
            smaller = min(y_1, y_2)
            for i in range(smaller, bigger + 1):
                if (x_1, i) in s:
                    overlaps.add((x_1, i))
                s.add((x_1, i))
        elif y_1 == y_2:
            bigger = max(x_1, x_2)
            smaller = min(x_1, x_2)
            for i in range(smaller, bigger + 1):
                if (i, y_1) in s:
                    overlaps.add((i, y_1))
                s.add((i, y_1))

print(len(overlaps))
