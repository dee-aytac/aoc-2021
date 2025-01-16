def find_floor(fname):
    with open(fname, 'r') as f:
        content = f.read().strip()
    floor = 0
    for char in content:
        if char == "(":
            floor += 1 
        elif char == ")":
            floor -= 1
    return floor

if __name__ == "__main__":
    print(find_floor('input.txt'))