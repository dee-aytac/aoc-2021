
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    total_yes_answers = 0
    group_yes_answers = set()
    for idx in range(len(content) + 1):
        try:
            line = content[idx]
        except: # for last line
            line = ""
        if line == "":
            total_yes_answers += len(group_yes_answers)
            print(len(group_yes_answers))
            group_yes_answers = set()
        else:
            group_yes_answers.update(set(line))
    return total_yes_answers

if __name__ == "__main__":
    print(solution('input.txt')) 
