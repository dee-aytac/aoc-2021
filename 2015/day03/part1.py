def find_houses(fname):
    x, y = 0, 0
    visited = set()
    visited.add((x, y))
    content = open(fname, 'r').read()
    for char in content:
        if char == ">":
            y += 1
        elif char == "<":
            y -= 1
        elif char == "v":
            x += 1
        elif char == "^":
            x -= 1 
        visited.add((x, y))
    return len(visited)
            
if __name__ == "__main__":
    print(find_houses('input.txt'))