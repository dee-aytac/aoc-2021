
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    total_steps_taken = 0
    idx = 0
    while True:
        if idx < 0 or idx > len(content) - 1:
            return total_steps_taken
        
        offset = int(content[idx])
        if offset >= 3:
            content[idx] = str(offset - 1)
        else:
            content[idx] = str(offset + 1)
        idx += offset
        total_steps_taken += 1

if __name__ == "__main__":
    print(solution('input.txt'))