
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

    for k in range(0,10):
        letter = [[0 for _ in range(5)] for _ in range(6)]
        for i in range(0, 6):
            for j in range(k*5+0, k*5+5):
                letter_j = j % 5
                letter[i][letter_j] = screen[i][j]
        for row in letter:
            for cell in row:
                if cell == 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print("      ")
        print("      ")
    return "finished"

if __name__ == "__main__":
    print(solution('input.txt'))