
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    acc = 0
    idx = 0
    executed = set()
    while idx < len(content):
        if idx in executed:
            return acc
        executed.add(idx)
        command, arg = content[idx].split(' ')
        if command == "acc":
            acc += int(arg)
            idx += 1
        elif command == "jmp":
            idx += int(arg)
        elif command == "nop":
            idx += 1
    return -1
    
if __name__ == "__main__":
    print(solution('input.txt')) 
