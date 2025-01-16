
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    visited = set()
    intersections = set()
    for line in content:
        commands = line.split(',')
        x, y = 0, 0
        for command in commands:
            direction, step = command[0], command[1:]
            course_horizontal = True
            if direction == "R":
                for s in range(int(step)):
                    y += 1
                    if (x, y, not course_horizontal) in visited:
                        intersections.add((x, y))
                    visited.add((x, y, course_horizontal))
            elif direction == "L":
                for s in range(int(step)):
                    y -= 1
                    if (x, y, not course_horizontal) in visited:
                        intersections.add((x, y))
                    visited.add((x, y, course_horizontal))
            elif direction == "D":
                course_horizontal = False
                for s in range(int(step)):
                    x += 1
                    if (x, y, not course_horizontal) in visited:
                        intersections.add((x, y))
                    visited.add((x, y, course_horizontal))
            elif direction == "U":
                course_horizontal = False
                for s in range(int(step)):
                    x -= 1
                    if (x, y, not course_horizontal) in visited:
                        intersections.add((x, y))
                    visited.add((x, y, course_horizontal))
    min_distance = float('inf')
    for point_x, point_y in intersections:
        curr_dist = (abs(point_x - 0) + abs(point_y - 0))
        if curr_dist < min_distance:
            min_distance = curr_dist
    return min_distance


if __name__ == "__main__":
    print(solution('input.txt')) 

