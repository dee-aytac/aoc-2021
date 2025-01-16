
def solution(fname, length):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')[0]
    for end, char in enumerate(content):
        start = end - length
        if start < 0:
            start = 0
        last_four_chars = content[start:end]
        if len(set(last_four_chars)) == length:
            return end
if __name__ == "__main__":
    print(solution('input.txt', 14)) 
