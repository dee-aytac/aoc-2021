import copy

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')[0]
    orig_memory = content.split(',')
    orig_memory = [int(num) for num in orig_memory]
    for noun in range(0, 100):
        for verb in range(0, 100):
            memory = copy.deepcopy(orig_memory)
            memory[1] = noun
            memory[2] = verb
            idx = 0
            while idx < len(memory):
                if memory[idx] == 99:
                    if memory[0] == 19690720:
                        return 100 * noun + verb
                    break
                if memory[idx] == 1:
                    memory[memory[idx + 3]] = memory[memory[idx + 1]] + memory[memory[idx + 2]]
                    idx += 4
                elif memory[idx] == 2:
                    memory[memory[idx + 3]] = memory[memory[idx + 1]] * memory[memory[idx + 2]]
                    idx += 4


if __name__ == "__main__":
    print(solution('input.txt')) 

