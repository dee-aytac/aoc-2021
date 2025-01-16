
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    answer = 0
    idx = 0
    values = dict()
    for key in ["a", "b", "c", "d"]:
        values[key] = 0
    while idx < len(content):
        line = content[idx]
        commands = line.split(' ')
        if commands[0] == "cpy":
            try:
                y = values[commands[1]]
            except:
                y = commands[1]
            values[commands[2]] = int(y)
            idx += 1
        elif commands[0] == "dec":
            values[commands[1]] -= 1
            idx += 1
        elif commands[0] == "inc":
            values[commands[1]] += 1
            idx += 1
        elif commands[0] == "jnz":
            try:
                x = values[commands[1]]
            except:
                x = commands[1]
            if x != 0:
                idx += int(commands[2])
            else:
                idx += 1
        # print(line, values)
    return values["a"]
    
if __name__ == "__main__":
    print(solution('input.txt'))