import numpy as np 

grid = np.zeros((1000, 1000), 'int8')

def find_on(fname):
    for line in open(fname):
        op = line.strip().split(' ')
        if op[0] == "toggle":
            c1, c2 = op[1], op[-1]
            x1, y1 = c1.split(',')
            x2, y2 = c2.split(',')
            x1, y1, x2, y2, = int(x1), int(y1), int(x2), int(y2)
            grid[x1:x2 + 1, y1:y2 + 1] = np.logical_not(grid[x1:x2 + 1, y1:y2 + 1])

        elif op[0] == "turn":
            c1, c2 = op[2], op[-1]
            x1, y1 = c1.split(',')
            x2, y2 = c2.split(',')
            x1, y1, x2, y2, = int(x1), int(y1), int(x2), int(y2)
            if op[1] == "on":
                grid[x1:x2 + 1, y1:y2 + 1] = 1    
            elif op[1] == "off":
                grid[x1:x2 + 1, y1:y2 + 1] = 0
    sum_ = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            if grid[i, j] == 1:
                sum_ += 1
    return sum_


if __name__ == "__main__":
    print(find_on('input.txt'))