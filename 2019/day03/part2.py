
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    visited = set()
    intersections = dict()
    steps = dict()
    for line in content:
        commands = line.split(',')
        x, y = 0, 0
        curr_step = 0
        for command in commands:
            direction, step = command[0], command[1:]
            course_horizontal = True
            if direction == "R":
                for s in range(int(step)):
                    y += 1
                    curr_step += 1
                    if (x, y, not course_horizontal) in visited:
                        intersections[(x, y)] = curr_step + steps[(x, y)]
                    steps[(x, y)] = curr_step
                    visited.add((x, y, course_horizontal))
            elif direction == "L":
                for s in range(int(step)):
                    y -= 1
                    curr_step += 1
                    if (x, y, not course_horizontal) in visited:
                        intersections[(x, y)] = curr_step + steps[(x, y)]
                    steps[(x, y)] = curr_step
                    visited.add((x, y, course_horizontal))
            elif direction == "D":
                course_horizontal = False
                for s in range(int(step)):
                    x += 1
                    curr_step += 1
                    if (x, y, not course_horizontal) in visited:
                        intersections[(x, y)] = curr_step + steps[(x, y)]
                    steps[(x, y)] = curr_step
                    visited.add((x, y, course_horizontal))
            elif direction == "U":
                course_horizontal = False
                for s in range(int(step)):
                    x -= 1
                    curr_step += 1
                    if (x, y, not course_horizontal) in visited:
                        intersections[(x, y)] = curr_step + steps[(x, y)]
                    steps[(x, y)] = curr_step
                    visited.add((x, y, course_horizontal))

    return sorted(intersections.values())[1]


if __name__ == "__main__":
    print(solution('input.txt')) 

