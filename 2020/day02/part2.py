
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    valid_pw = 0
    for line in content:
        p1, password = line.split(': ')
        repeat_limits, char = p1.split(' ')
        pos_1, pos_2 = repeat_limits.split('-')
        if ((password[int(pos_1) - 1] == char and password[int(pos_2) - 1] != char) or 
        (password[int(pos_1) - 1] != char and password[int(pos_2) - 1] == char )):
            valid_pw += 1
    return valid_pw

if __name__ == "__main__":
    print(solution('input.txt')) 

