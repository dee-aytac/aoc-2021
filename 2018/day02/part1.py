
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    threes = 0
    twos = 0
    for line in content:
        chars = set()
        for char in line:
            chars.add(char)
        found_twos = False
        found_threes = False
        for char in chars:
            count_char = line.count(char)
            if count_char == 2:
                found_twos = True
            if count_char == 3:
                found_threes = True

        if found_twos:
            twos += 1
        if found_threes:
            threes += 1
    return threes * twos

if __name__ == "__main__":
    print(solution('input.txt'))