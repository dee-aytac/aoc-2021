
def solution(fname, goals):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    signal_strengts = dict()
    cycle = 0
    value_x = 1
    for line in content:
        if "noop" == line:
            cycle += 1
        else:
            step = line.split(' ')[1]
            cycle += 1
            if cycle in goals:
                signal_strengts[cycle] = value_x * cycle
            cycle += 1
            value_x += int(step)
        if cycle in goals:
            signal_strengts[cycle] = value_x * cycle
        
    return sum(signal_strengts.values())
if __name__ == "__main__":
    print(solution('sample.txt', [20, 60, 100, 140, 180, 220])) 
