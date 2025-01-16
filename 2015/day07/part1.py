

def evaluate(values, operations):
    i = 0
    while True:
        if i >= len(operations):
            i = 0
        message = operations[i]
        processed = False
        p1, goal_wire = message.split(" -> ")
        first_part = p1.split(' ')
        if len(first_part) == 1:
            value = first_part[0]
            if value in values:
                if values[value] != "NA":
                    values[goal_wire] = int(values[value])
                    processed = True
            else:
                values[goal_wire] = int(value)
                processed = True

        elif len(first_part) == 2:
            opr, opd = p1.split(' ')
            if opr == "NOT":
                if values[opd] != "NA":
                    values[goal_wire] = int(65535 - values[opd])
                    processed = True
        else:
            opd1, opr , opd2 = p1.split(' ')
            if opd1 in values:
                if values[opd1] == "NA":
                    i += 1
                    continue
            if opd2 in values:
                if values[opd2] == "NA":
                    i += 1
                    continue
            if opr == "AND":
                if opd1 in values and opd2 in values:
                    values[goal_wire] = values[opd1] & values[opd2]
                    processed = True
                elif opd1 in values:
                    values[goal_wire] = values[opd1] & int(opd2)
                    processed = True

                elif opd2 in values:
                    values[goal_wire] = int(opd1) & values[opd2]
                    processed = True
                else:
                    values[goal_wire] = int(opd1) & int(opd2)
                    processed = True

            elif opr == "OR":
                values[goal_wire] = values[opd1] | values[opd2]
                processed = True
            elif opr == "LSHIFT":
                values[goal_wire] = values[opd1] << int(opd2)
                processed = True
            elif opr == "RSHIFT":
                values[goal_wire] = values[opd1] >> int(opd2)
                processed = True


        if processed:
            operations.pop(i)
        
        i += 1          

        if len(operations) == 0:
            break

    return values

def main(p_input):
    operations = list()
    values = dict()
    for line in open(p_input):
        operations.append(line.strip('\n'))
        values[line.strip('\n').split(" -> ")[1]] = "NA"
    operations = sorted(operations, key = len)
    result = evaluate(values, operations)
    return result['a']

if __name__ == "__main__":
    print(main("input.txt"))