
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    valid_passport = 0
    passport_data = dict()
    idx = 0
    for line in content:
        if line == "":
            if len(passport_data.keys()) == 8 or (len(passport_data.keys()) == 7 and "cid" not in passport_data.keys()):
                valid_passport += 1
            passport_data = dict()
            idx += 1
            continue
        fields = line.split(' ')
        for field in fields:
            key, val = field.split(':')
            passport_data[key] = val

    return valid_passport + 1

if __name__ == "__main__":
    print(solution('input.txt')) 
