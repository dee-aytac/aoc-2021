import collections

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    total_sum = 0
    for line in content:
        letters, listed = line.split('[')
        letters = letters.split('-')
        sector_id = letters[-1]
        letters = letters[:-1]
        str_letters = ""
        for part in letters:
            str_letters += part
        listed = listed[:-1]
        key = "".join([k for k, v in sorted(collections.Counter(str_letters).most_common(), key=lambda e: (-e[1], e[0]))[:5]])
        if key == listed:
            print(str_letters, "passed")
            total_sum += int(sector_id)       


    return total_sum
if __name__ == "__main__":
    print(solution('input.txt'))