import string

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    values = string.ascii_lowercase + string.ascii_uppercase
    total_sum = 0
    for line in content:
        p1, p2 = line[0:len(line)//2], line[len(line)//2:]
        common_chars = list(set(p1).intersection(set(p2)))
        total_sum += sum([1 + values.index(char) for char in common_chars])
    return total_sum
    
if __name__ == "__main__":
    print(solution('input.txt')) 
