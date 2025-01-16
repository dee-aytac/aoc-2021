def change_screen(screen, cycle, pos):
    draw_x = (cycle) // 40
    draw_y = (cycle) % 40
    if draw_y - 1 == pos:
        screen[draw_x][pos + 1] = "#"
    if draw_y == pos:
        screen[draw_x][pos] = "#"
    if draw_y + 1 == pos:
        screen[draw_x][pos - 1] = "#"


def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    cycle = 0
    value_x = 1
    screen = [["." for _ in range(40)] for _ in range(6)]
    for line in content:
        if "noop" == line:
            cycle += 1
        else:
            step = line.split(' ')[1]
            cycle += 1
            change_screen(screen, cycle, value_x)
            cycle += 1
            value_x += int(step)
        change_screen(screen, cycle, value_x)
    # print screen
    for row in screen:
        for col in row:
            print(col, end=" ")
        print()

if __name__ == "__main__":
    print(solution('input.txt')) 