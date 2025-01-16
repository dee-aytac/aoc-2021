def solution(fname):
    with open(fname) as f:
        content = f.read().splitlines()
    registers = {"a": 0, "b": 0}
    instructions = list()
    for line in content:
        instructions.append(line)
    idx = 0
    while idx < len(instructions):
        inst = instructions[idx]
        if ',' in inst:
            op, r = inst.split(',')
            p1, p2 = op.split(' ')
            if p1 == "jie":
                if registers[p2] % 2 == 0:
                    idx += int(r) - 1
            elif p1 == "jio":
                if registers[p2] == 1:
                    idx += int(r) - 1
        else:
            p1, p2 = inst.split(' ')
            if p1 == "hlf":
                registers[p2] /=  2 
            elif p1 == "tpl":
                registers[p2] *= 3
            elif p1 == "inc":
                registers[p2] += 1
            elif p1 == "jmp":
                idx += int(p2) - 1
        idx += 1
    return registers
    
if __name__ == "__main__":
    print(solution("input.txt"))

