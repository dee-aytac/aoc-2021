def find_houses(fname):
    x_s, y_s = 0, 0
    x_r, y_r = 0, 0
    visited = set()
    visited.add((0, 0))
    content = open(fname, 'r').read()
    idx = 0
    while idx < len(content):
        char = content[idx]
        if char == ">":
            y_s += 1
        elif char == "<":
            y_s -= 1
        elif char == "v":
            x_s += 1
        elif char == "^":
            x_s -= 1
        visited.add((x_s, y_s))

        char = content[idx + 1]
        if char == ">":
            y_r += 1
        elif char == "<":
            y_r -= 1
        elif char == "v":
            x_r += 1
        elif char == "^":
            x_r -= 1
        visited.add((x_r, y_r))
        idx += 2
    return len(visited) 
            
if __name__ == "__main__":
    print(find_houses('input.txt'))