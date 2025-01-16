
def move(command, position):
    if command == "U":
        if position != 1 and position != 2 and position != 3:
            position = position - 3
    elif command == "L":
        if position != 1 and position != 4 and position != 7:
            position = position - 1
    elif command == "R":
        if position != 3 and position != 6 and position != 9:
            position = position + 1
    elif command == "D":
        if position != 7 and position != 8 and position != 9:
            position = position + 3
    return position

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    button = 5
    code = ""
    for idx, line in enumerate(content):
        for char in line:
            button = move(char, button)
        code += str(button) 
    return code

if __name__ == "__main__":
    print(solution('input.txt'))