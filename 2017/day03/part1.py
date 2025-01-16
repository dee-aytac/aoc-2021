
# middle is 0,0 where num = 1
def solution(inp):
    num = 2
    layer = 3
    pos_x, pos_y = 1, 0
    while True:
        while True:
            for _ in range(layer - 2): # going up
                if num == inp:
                    return abs(pos_x) + abs(pos_y)
                num += 1
                pos_y -= 1

            for _ in range(layer - 1): # going left
                if num == inp:
                    return abs(pos_x) + abs(pos_y)
                num += 1
                pos_x -= 1

            for _ in range(layer - 1): # going down
                if num == inp:
                    return abs(pos_x) + abs(pos_y)
                num += 1
                pos_y += 1

            for _ in range(layer): # going right
                if num == inp:
                    return abs(pos_x) + abs(pos_y)
                num += 1
                pos_x += 1
            break

        layer += 2

if __name__ == "__main__":
    print(solution(289326))