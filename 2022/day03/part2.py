import string

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    values = string.ascii_lowercase + string.ascii_uppercase
    total_sum = 0
    for idx in range(0, len(content) - 2, 3):
        common_chars = list((set(content[idx]).intersection(set(content[idx+1]))).intersection(content[idx + 2]))
        total_sum += sum([1 + values.index(char) for char in common_chars])
    return total_sum
    
if __name__ == "__main__":
    print(solution('input.txt')) 
