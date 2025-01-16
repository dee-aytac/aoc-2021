def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip()
    commands = content.split(', ')
    x = 0
    y = 0
    visited = set()
    direction = 0 # 0: North, 1: East, 2: South 3: West
    for command in commands:
        if command[0] == "R":
            direction = (direction + 1) % 4
        elif command[0] == "L":
            direction = (direction - 1) % 4
        step = int(command[1:])
        if direction == 0:
            for _ in range(step):
                x = x - 1
                if (x, y) in visited:
                    return (abs)(x-0) + (abs)(y-0)
                else:
                    visited.add((x, y))
        elif direction == 1:
            for _ in range(step):
                y = y + 1
                if (x, y) in visited:
                    return (abs)(x-0) + (abs)(y-0)
                else:
                    visited.add((x, y))
        elif direction == 2:
            for _ in range(step):
                x = x + 1
                if (x, y) in visited:
                    return (abs)(x-0) + (abs)(y-0)
                else:
                    visited.add((x, y))
        elif direction == 3:
            for _ in range(step):
                y = y - 1
                if (x, y) in visited:
                    return (abs)(x-0) + (abs)(y-0)
                else:
                    visited.add((x, y))

if __name__ == "__main__":
    print(solution('input.txt'))