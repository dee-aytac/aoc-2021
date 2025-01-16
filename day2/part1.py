x_pos = 0
depth = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        command, operand = line.split(' ')
        operand = int(operand)
        if command == "forward":
            x_pos += operand
        elif command == "down":
            depth += operand
        elif command == "up":
            depth -= operand
        
print(x_pos)
print(depth)