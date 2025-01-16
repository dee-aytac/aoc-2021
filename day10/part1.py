lines = []
for line in open('input.txt'):
    lines.append(line.strip())

open_brackets = ['(', '[', '{', '<']
close_brackets = [')', ']', '}', '>']
points = {')': 0, ']': 0, '}': 0, '>': 0}
for line in lines:
    stack = []
    for char in line:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            opener = stack.pop()
            index = close_brackets.index(char)
            if opener != open_brackets[index]:
                points[char] += 1
                break
print(points[')'] * 3 + points[']'] * 57 + points['}'] * 1197 + points['>'] * 25137)