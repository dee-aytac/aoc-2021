from copy import deepcopy

def move_tail(tail_pos, head_pos):
    orig_tail_pos = deepcopy(tail_pos)
    x_dir = head_pos[0] - tail_pos[0]
    y_dir = head_pos[1] - tail_pos[1]
    if x_dir != 0:
        tail_pos[0] += (x_dir // abs(x_dir))
    if y_dir != 0:
        tail_pos[1] += (y_dir // abs(y_dir))
    if tail_pos == head_pos:
        return orig_tail_pos 
        visited_by_tail.add((orig_tail_pos[0], orig_tail_pos[1]))

    visited_by_tail.add((tail_pos[0], tail_pos[1]))
    return tail_pos


def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0
    global visited_by_tail
    visited_by_tail = set()
    for line in content:
        direction, step = line.split(' ')
        if direction == "R":
            for _ in range(int(step)):
                head_y += 1
                tail_x, tail_y = move_tail([tail_x, tail_y], [head_x, head_y])
        elif direction == "L":
            for _ in range(int(step)):
                head_y -= 1
                tail_x, tail_y = move_tail([tail_x, tail_y], [head_x, head_y])    

        elif direction == "U":
            for _ in range(int(step)):
                head_x -= 1
                tail_x, tail_y = move_tail([tail_x, tail_y], [head_x, head_y])

        elif direction == "D":
            for _ in range(int(step)):
                head_x += 1
                tail_x, tail_y = move_tail([tail_x, tail_y], [head_x, head_y])
    return len(visited_by_tail)
if __name__ == "__main__":
    print(solution('input.txt')) 
