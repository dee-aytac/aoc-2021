
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    valid_pw = 0
    for line in content:
        p1, password = line.split(': ')
        repeat_limits, char = p1.split(' ')
        repeat_low, repeat_up = repeat_limits.split('-')
        char_range = [num for num in range(int(repeat_low), int(repeat_up) + 1)]
        if password.count(char) in char_range:
            valid_pw += 1
    return valid_pw

if __name__ == "__main__":
    print(solution('input.txt')) 

