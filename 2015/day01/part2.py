def find_floor(fname):
    with open(fname, 'r') as f:
        content = f.read().strip()
    floor = 0
    for idx, char in enumerate(content):
        if char == "(":
            floor += 1 
        elif char == ")":
            floor -= 1
        if floor == -1:
            return idx + 1

if __name__ == "__main__":
    print(find_floor('input.txt'))