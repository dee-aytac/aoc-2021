


def solution(fname, rows):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')[0]
    safe_tiles = content.count(".")
    last_row = content
    row_length = len(last_row)
    grid = list()
    grid.append(last_row)
    for _ in range(rows - 1):
        new_row = ""
        for idx in range(row_length):
            if idx == 0:
                left_safe = True # do not change
                center_safe = True
                right_safe = True
                if last_row[idx] == "^":
                    center_safe = False
                if last_row[idx + 1] == "^":
                    right_safe = False

            elif idx == row_length - 1:
                left_safe = True
                center_safe = True
                right_safe = True # do not change
                if last_row[idx - 1] == "^":
                    left_safe = False
                if last_row[idx] == "^":
                    center_safe = False
            else:
                left_safe = True
                center_safe = True
                right_safe = True
                if last_row[idx - 1] == "^":
                    left_safe = False
                if last_row[idx] == "^":
                    center_safe = False
                if last_row[idx + 1] == "^":
                    right_safe = False

            if left_safe == False and center_safe == False and right_safe == True:
                new_row += "^"

            elif right_safe == False and center_safe == False and left_safe == True:
                new_row += "^"

            elif right_safe == True and center_safe == True and left_safe == False:
                new_row += "^"

            elif right_safe == False and center_safe == True and left_safe == True:
                new_row += "^"
            else:
                new_row += "."
                safe_tiles += 1
        grid.append(new_row)
        last_row = new_row
        
    return safe_tiles
if __name__ == "__main__":
    print(solution('input.txt', 40))