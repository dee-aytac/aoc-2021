with open('input.txt', 'r') as f:
    gamma = ""
    epsilon = ""
    lines = f.read().splitlines()
    for i in range(len(lines[0])):
        zeros = 0
        ones = 0
        for j in range(len(lines)):
            line = lines[j]
            if line[i] == "1":
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma * epsilon)

