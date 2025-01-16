
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    rows = 6
    cols = 50
    screen = [[0 for _ in range(cols)] for _ in range(rows)]
    for line in content:
        to_add = list()
        commands = line.split(' ')
        if commands[0] == "rect":
            x, y = commands[1].split("x")
            for i in range(int(y)):
                for j in range(int(x)):
                    screen[i][j] = 1
        else:
            step = int(commands[4])
            row_or_col_no = int(commands[2].split("=")[1])
            if commands[1] == "row":
                i = row_or_col_no
                for j in range(cols):
                    if screen[i][j] == 1:
                        to_add.append((i, j + step))
                        screen[i][j] = 0

            elif commands[1] == "column":
                j = row_or_col_no
                for i in range(rows):
                    if screen[i][j] == 1:
                        to_add.append(((i + step), j))
                        screen[i][j] = 0

        for (r, c) in to_add:
            r = (r % rows)
            c = (c % cols)
            screen[r][c] = 1

    total_lit = 0
    for row in screen:
        for cell in row:
            if cell == 1:
                total_lit += 1
    return total_lit

if __name__ == "__main__":
    print(solution('input.txt'))