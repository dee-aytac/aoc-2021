
# 0 position mode
# 1, imm mode
def get_memory(memory, idx, mode):
    if mode == 1:
        return memory[idx]
    if mode == 0:
        return memory[memory[idx]]

def solution(fname, inp):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')[0]
    memory = content.split(',')
    memory = [int(num) for num in memory]
    idx = 0
    while idx < len(memory):
        param_mode = False
        if len(str(memory[idx])) > 1:
            opcode = int(str(memory[idx])[-1])
            param_mode = True
        else:
            opcode = memory[idx]
        if opcode == 99:
            break
        if opcode == 1:
            if param_mode:
                memory[memory[idx + 3]] = get_memory(memory, idx + 1, (memory[idx] // 100) % 10) + get_memory(memory, idx + 2, memory[idx] // 1000)
            else:
                memory[memory[idx + 3]] = memory[memory[idx + 1]] + memory[memory[idx + 2]]

            idx += 4
        elif opcode == 2:
            if param_mode:
                memory[memory[idx + 3]] = get_memory(memory, idx + 1, (memory[idx] // 100) % 10) * get_memory(memory, idx + 2, memory[idx] // 1000)
            else:
                memory[memory[idx + 3]] = memory[memory[idx + 1]] * memory[memory[idx + 2]]
            idx += 4
        elif opcode == 3:
            memory[memory[idx + 1]] = inp
            idx += 2
        elif opcode == 4:
            print(memory[memory[idx + 1]])
            idx += 2
        elif opcode == 5:
            if get_memory(memory, idx + 1, (memory[idx] // 100) % 10) != 0:
                idx = get_memory(memory, idx + 2, memory[idx] // 1000)
            else:
                idx += 3
        elif opcode == 6:
            if get_memory(memory, idx + 1, (memory[idx] // 100) % 10) == 0:
                idx = get_memory(memory, idx + 2, memory[idx] // 1000)
            else:
                idx += 3
        elif opcode == 7:
            if get_memory(memory, idx + 1, (memory[idx] // 100) % 10) < get_memory(memory, idx + 2, memory[idx] // 1000):
                memory[memory[idx + 3]] = 1
            else:
                memory[memory[idx + 3]] = 0
            if memory[memory[idx + 3]] != idx:
                idx += 4
        elif opcode == 8:
            if get_memory(memory, idx + 1, (memory[idx] // 100) % 10) == get_memory(memory, idx + 2, memory[idx] // 1000):
                memory[memory[idx + 3]] = 1
            else:
                memory[memory[idx + 3]] = 0
            if memory[memory[idx + 3]] != idx:
                idx += 4
        else:
            return "finished"
            idx += 1

if __name__ == "__main__":
    print(solution('input.txt', 5)) 

