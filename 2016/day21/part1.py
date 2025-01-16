from collections import deque

def solution(fname, inp):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    inp = [char for char in inp]
    new_string = inp
    for line in content:
        args = line.split(' ')
        if args[0] == "rotate":
            if len(args) == 4:
                side, step = args[1], int(args[2])
                if side == "left":
                    step *= -1
                to_rotate = deque(new_string)
                to_rotate.rotate(step)
                new_string = list(to_rotate)
            else:
                letter = args[-1]
                step = new_string.index(letter)
                if step >= 4:
                    step += 1
                step += 1
                to_rotate = deque(new_string)
                to_rotate.rotate(step)
                new_string = list(to_rotate)
        elif args[0] == "swap":
            x, y = args[2], args[5]
            new_string = inp
            if args[1] == "position":
                new_string[int(x)], new_string[int(y)] = new_string[int(y)], new_string[int(x)]
            elif args[1] == "letter":
                x_index = new_string.index(x)
                y_index = new_string.index(y)
                new_string[x_index] = y
                new_string[y_index] = x
        elif args[0] == "reverse":
            x, y = int(args[2]), int(args[4])
            new_string = new_string[:x] + list(reversed(new_string[x:y+1])) + new_string[y+1:]
        elif args[0] == "move":
            x, y = int(args[2]), int(args[5])
            new_string = inp
            char = new_string.pop(x)
            new_string.insert(y, char)
        else:
            new_string = "-1"
            print("unknown command", args[0])
        inp = new_string   
        #print(line, "->>", "".join(inp))
    return "".join(inp)

if __name__ == "__main__":
    print(solution('input.txt', "abcdefgh"))