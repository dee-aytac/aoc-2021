lines = []
for line in open('input.txt'):
    lines.append(line.strip())

open_brackets = ['(', '[', '{', '<']
close_brackets = [')', ']', '}', '>']
points = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []
for line in lines:
    stack = []
    local_score = 0
    for char in line:
        if char in open_brackets:
            stack.append(char)
        else:
            opener = stack.pop()
            index = close_brackets.index(char)
            if opener != open_brackets[index]:
                break
    else:
        while len(stack) > 0:
            char = stack.pop()
            index = open_brackets.index(char)
            local_score = local_score *  5 + points[close_brackets[index]]
    if local_score:
        scores.append(local_score)
scores.sort()
mid = len(scores) // 2
print(scores[mid])