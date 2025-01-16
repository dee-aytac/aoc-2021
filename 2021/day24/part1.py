x = 9999999999999
print(x)
#msg = "13579246899999"
#ctr = 0
values = {"w": 0, "x": 0, "y": 0, "z": 0}
for i in range(99999999999999, 11111111111111, -1):
    msg = str(i)
    ctr = 0
    if "0" in msg:
        continue
    for l in open('input.txt'):
        line = l.strip()
        command = line[:3]
        if command == "inp":
            op = line[-1]
            #print(command, op)
            values[op] = int(msg[ctr])
            ctr += 1
        else:
            op1, op2 = line[4:].split(' ')
            try:
                op2 = int(op2)
            except:
                op2 = str(op2)
            #print(command, op1, op2)
            if command == "add":
                if isinstance(op2, int):
                    values[op1] += int(op2)
                else:
                    values[op1] += values[op2]
            elif command == "mul":
                if isinstance(op2, int):
                    values[op1] *= int(op2)
                else:
                    values[op1] *= values[op2]  
            elif command == "div":
                if isinstance(op2, int):
                    values[op1] /= int(op2)
                else:
                    values[op1] /= values[op2]
            elif command == "mod":
                if isinstance(op2, int):
                    values[op1] = values[op1] % int(op2)
                else:
                    values[op1] = values[op1] % values[op2]
            elif command == "eql":
                if isinstance(op2, int):
                    ans = values[op1] == op2
                else:
                    ans = values[op1] == values[op2]
                values[op1] = ans
    #print(values["z"])
    # if int(values["z"]) == 0:
    #     print(i)
    #     break
print(values["z"] == 0)
