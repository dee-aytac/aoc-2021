
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    answer = 0
    for line in content:
        code_inside_bracket = False
        correct_code = False
        inside_bracket = False
        for idx, char in enumerate(line):
            if code_inside_bracket:
                break
            if line[idx] == "[":
                inside_bracket = True
            code = ""
            for i in range(0, 4):
                try:
                    code += line[idx + i]
                except:
                    break
            if len(code) != 4:
                break
            if code[0] == code[3] and code[1] == code[2] and code[0] != code[1]:
                if inside_bracket:
                    code_inside_bracket = True
                else:
                    correct_code = True
            if line[idx] == "]":
                inside_bracket = False
        if code_inside_bracket == False and correct_code == True:
            answer += 1
    return answer
    
if __name__ == "__main__":
    print(solution('input.txt'))