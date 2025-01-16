def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    valid_pass = 0
    for line in content:
        phrases = line.split(' ')
        phrases = [''.join(sorted(ph)) for ph in phrases]
        valid = True
        for phrase in phrases:
            if phrases.count(phrase) > 1:
                valid = False
        if valid:
            valid_pass += 1
    return valid_pass

if __name__ == "__main__":
    print(solution('input.txt'))