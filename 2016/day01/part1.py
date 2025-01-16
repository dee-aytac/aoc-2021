def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip()
    commands = content.split(', ')
    x = 0
    y = 0
    direction = 0 # 0: North, 1: East, 2: South 3: West
    for command in commands:
        if command[0] == "R":
            direction = (direction + 1) % 4
        elif command[0] == "L":
            direction = (direction - 1) % 4
        step = int(command[1:])
        if direction == 0:
            x = x - step

        elif direction == 1:
            y = y + step

        elif direction == 2:
            x = x + step

        elif direction == 3:
            y = y - step
    return (abs)(x-0) + (abs)(y-0)

if __name__ == "__main__":
    print(solution('input.txt'))