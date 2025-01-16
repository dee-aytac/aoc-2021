from copy import deepcopy

def move_tail(ropes, head_x, head_y):
    new_ropes = list()
    for idx, (tail_x, tail_y) in enumerate(ropes):
        x_dir = head_x - tail_x
        y_dir = head_y - tail_y
        new_tail_x, new_tail_y = tail_x, tail_y
        if x_dir != 0:
            new_tail_x += (x_dir // abs(x_dir))
        if y_dir != 0:
            new_tail_y += (y_dir // abs(y_dir))

        if [new_tail_x, new_tail_y] == [head_x, head_y]:
            new_ropes.append([tail_x, tail_y])
            head_x, head_y = tail_x, tail_y
        else:
            new_ropes.append([new_tail_x, new_tail_y])
            head_x, head_y = new_tail_x, new_tail_y
    visited_by_tail.add((new_ropes[-1][0], new_ropes[-1][1]))
    return new_ropes

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    head_x, head_y = 0, 0
    ropes = [[0, 0] for _ in range(0, 9)]
    global visited_by_tail
    visited_by_tail = set()
    for line in content:
        direction, step = line.split(' ')
        if direction == "R":
            for _ in range(int(step)):
                head_y += 1
                ropes = move_tail(ropes, head_x, head_y)

        elif direction == "L":
            for _ in range(int(step)):
                head_y -= 1
                ropes = move_tail(ropes, head_x, head_y)

        elif direction == "U":
            for _ in range(int(step)):
                head_x -= 1
                ropes = move_tail(ropes, head_x, head_y)

        elif direction == "D":
            for _ in range(int(step)):
                head_x += 1
                ropes = move_tail(ropes, head_x, head_y)

    return len(visited_by_tail)
if __name__ == "__main__":
    print(solution('input.txt')) 
