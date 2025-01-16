from copy import deepcopy

def solution(fname):
    with open(fname, 'r') as f:
        original_content = f.read().strip().split('\n')
    jump_ops = [idx for idx, line in enumerate(original_content) if "jmp" in line]
    nop_ops = [idx for idx, line in enumerate(original_content) if "nop" in line]
    while True:
        content = deepcopy(original_content)
        if len(jump_ops) > 0:
            op_idx = jump_ops.pop()
            content[op_idx] = content[op_idx].replace("jmp", "nop")
        else:
            op_idx = nop_ops.pop()
            content[op_idx] = content[op_idx].replace("nop", "jmp")
        idx = 0
        executed = set()
        acc = 0
        while idx < len(content):
            if idx in executed:
                break
            executed.add(idx)
            command, arg = content[idx].split(' ')
            if command == "acc":
                acc += int(arg)
                idx += 1
            elif command == "jmp":
                idx += int(arg)
            elif command == "nop":
                idx += 1
        if idx == len(original_content):
            return acc
    
if __name__ == "__main__":
    print(solution('input.txt')) 
