from collections import Counter

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    answer = ""
    idx_col = 0
    for _ in range(len(content[0])):
        column_str = ""
        for idx_row in range(len(content)):
            column_str += content[idx_row][idx_col]
        idx_col += 1
        column_list = Counter(column_str)
        answer += column_list.most_common()[-1][0]
    return answer
if __name__ == "__main__":
    print(solution('input.txt'))