
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')[0]
    level = 0
    points = 0
    idx = 0
    inside_garbage = False
    while idx < len(content):
        char = content[idx]
        if char == "<":
            inside_garbage = True
        elif char == ">":
            inside_garbage = False
        elif char == "!":
            idx += 1
        if not inside_garbage:
            if char == "{":
                level += 1
            elif char == "}":
                points += level
                level -= 1
        idx += 1
    return points

if __name__ == "__main__":
    print(solution('input.txt')) 
