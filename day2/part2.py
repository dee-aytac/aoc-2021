x_pos = 0
depth = 0
aim = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        command, operand = line.split(' ')
        operand = int(operand)
        if command == "forward":
            x_pos += operand
            depth += aim * operand
        elif command == "down":
            aim += operand
        elif command == "up":
            aim -= operand
        
print(x_pos)
print(depth)
print(x_pos * depth)