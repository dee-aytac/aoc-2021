
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')[0]
    memory = content.split(',')
    memory = [int(num) for num in memory]
    #
    memory[1] = 12
    memory[2] = 2
    #
    idx = 0
    while idx < len(memory):
        if memory[idx] == 99:
            break
        if memory[idx] == 1:
            memory[memory[idx + 3]] = memory[memory[idx + 1]] + memory[memory[idx + 2]]
            idx += 4
        elif memory[idx] == 2:
            memory[memory[idx + 3]] = memory[memory[idx + 1]] * memory[memory[idx + 2]]
            idx += 4
        else:
            idx += 1
    return memory[0]

if __name__ == "__main__":
    print(solution('input.txt')) 

