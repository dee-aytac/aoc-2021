
def get_neighbours_sum(pos_x, pos_y, grid):
    total_sum = 0
    for x in [0, -1, 1]:
        for y in [0, -1, 1]:
            rr = pos_x + x
            cc = pos_y + y
            if (rr, cc) in grid.keys():
                total_sum += grid[(rr, cc)]
    return total_sum

# middle is 0,0 where num = 1
def solution(inp):
    num = 2
    layer = 3
    pos_x, pos_y = 1, 0
    grid = dict()
    grid[(0, 0)] = 1
    while True:
        while True:
            for _ in range(layer - 2): # going up
                num = get_neighbours_sum(pos_x, pos_y, grid)
                grid[(pos_x,pos_y)] = num
                if num >= inp:
                    return pos_x, pos_y, num
                pos_y -= 1

            for _ in range(layer - 1): # going left
                num = get_neighbours_sum(pos_x, pos_y, grid)
                grid[(pos_x,pos_y)] = num
                if num >= inp:
                    return pos_x, pos_y, num
                pos_x -= 1

            for _ in range(layer - 1): # going down
                num = get_neighbours_sum(pos_x, pos_y, grid)
                grid[(pos_x,pos_y)] = num
                if num >= inp:
                    return pos_x, pos_y, num
                pos_y += 1

            for _ in range(layer): # going right
                num = get_neighbours_sum(pos_x, pos_y, grid)
                grid[(pos_x,pos_y)] = num
                if num >= inp:
                    return pos_x, pos_y, num
                pos_x += 1
                
            break
        layer += 2

if __name__ == "__main__":
    print(solution(289326)[2])