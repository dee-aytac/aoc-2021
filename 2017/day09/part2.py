
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')[0]
    level = 0
    garbages = 0
    idx = 0
    inside_garbage = False
    while idx < len(content):
        char = content[idx]
        if char == "<":
            if inside_garbage:
                garbages += 1
            else:
                inside_garbage = True
        elif char == ">":
            inside_garbage = False
        elif char == "!":
            idx += 1
        else:
            if inside_garbage:
                garbages += 1



        idx += 1
    return garbages

if __name__ == "__main__":
    print(solution('input.txt')) 
