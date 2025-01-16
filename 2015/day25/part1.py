def get_next_value(n):
    return (n * 252533) % 33554393

def get_actual_no(inp_row, inp_col):
    layer = 1
    current_no = 1
    while True:
        col = 1
        row = layer
        while row > 0:
            row -= 1
            col += 1
            current_no += 1
            if row == inp_row and col == inp_col:
                return current_no
        layer += 1

def solution(x):
    i = 1
    no = 20151125
    while i < x:
        no = get_next_value(no)
        i += 1
    return no

if __name__ == "__main__":
    get_actual_no = get_actual_no(2981, 3075)
    print(solution(18331560))