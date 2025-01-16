def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    registers = dict()
    max_value_yet = float('-inf')
    for line in content:
        action, condition = line.split(" if ")
        action = action.split(' ')
        condition = condition.split(' ')
        dest = action[0]
        num_to_add = int(action[2])
        if action[1] == "dec":
            num_to_add *= -1
        src = condition[0]
        check_operator, check_num = condition[1], int(condition[2])
        if dest not in registers.keys():
            registers[dest] = 0
        if src not in registers.keys():
            registers[src] = 0
        #
        take_action = False
        if check_operator == "==":
            if registers[src] == check_num:
                take_action = True
        elif check_operator == ">":
            if registers[src] > check_num:
                take_action = True
        elif check_operator == ">=":
            if registers[src] >= check_num:
                take_action = True
        elif check_operator == "<":
            if registers[src] < check_num:
                take_action = True       
        elif check_operator == "<=":
            if registers[src] <= check_num:
                take_action = True     
        elif check_operator == "!=":
            if registers[src] != check_num:
                take_action = True  
        if take_action:
            registers[dest] += num_to_add
        if registers[dest] > max_value_yet:
            max_value_yet = registers[dest]
        #print(action, condition)

    return max_value_yet

if __name__ == "__main__":
    print(solution('input.txt'))