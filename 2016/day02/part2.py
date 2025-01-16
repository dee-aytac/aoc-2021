
def move(command, position):
    if command == "U":
        if position != 1 and position != 2 and position != 4 and position != 5 and position != 9:
            if position == 3 or position == 13:
                position -= 2
            else:
                position -= 4
    elif command == "L":
        if position != 1 and position != 2 and position != 5 and position != 10 and position != 13:
            position = position - 1
    elif command == "R":
        if position != 1 and position != 4 and position != 9 and position != 12 and position != 13:
            position = position + 1
    elif command == "D":
        if position != 5 and position != 9 and position != 10 and position != 12 and position != 13:
            if position == 1 or position == 11:
                position += 2
            else:
                position += 4
    return position

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    button = 5
    code = ""
    for idx, line in enumerate(content):
        for char in line:
            button = move(char, button)
        if button >= 10:
            code += chr(55+button)
        else:
            code += str(button) 
    return code

if __name__ == "__main__":
    print(solution('input.txt'))