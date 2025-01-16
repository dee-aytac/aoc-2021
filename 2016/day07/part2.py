
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    answer = 0
    for line in content:
        other_content = line
        bracket_content = ""
        while '[' in other_content:
            i1, i2 = other_content.index('['), other_content.index(']')
            bracket_content += other_content[i1 + 1 : i2]
            other_content = other_content[0:i1] + other_content[i2+1:]
        correct_code = False
        next_code = list()
        inside_bracket = False
        answer_found_in_line = False
        for idx, char in enumerate(other_content):
            code = ""
            for i in range(0, 3):
                try:
                    code += other_content[idx + i]
                except:
                    break
            if len(code) != 3:
                break
            if code[0] == code[2] and code[0] != code[1]:
                next_code.append(code[1] + code[0]+ code[1])
        for c in next_code:
            if c in bracket_content:
                answer_found_in_line = True
        if answer_found_in_line == True:
            answer += 1
    return answer

if __name__ == "__main__":
    print(solution('input.txt'))