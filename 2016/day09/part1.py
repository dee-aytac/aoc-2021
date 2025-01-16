import collections

def get_dims(text, current_idx):
    repeat = ""
    char_number = ""
    found_repeat = False
    found_char_no = False
    current_idx += 1
    while current_idx < len(text) and found_repeat == False:
        if found_char_no == False:
            if text[current_idx] == "x":
                found_char_no = True
            else:
                char_number += text[current_idx]
        else:
            if text[current_idx] == ")":
                found_repeat = True
            else:
                repeat += text[current_idx]
        current_idx += 1

    return int(repeat), int(char_number), current_idx


def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')[0]
    total_length = 0
    strinq = ""
    idx = 0
    while idx < len(content):
        if content[idx] in ["", " ", "\n", "\r", "\r", "\r\”"]:
            idx += 1
        if content[idx] == "(":
            repeat, char_length, idx = get_dims(content, idx)
            repeat_pattern = content[idx: idx + char_length]
            for _ in range(repeat):
                strinq += repeat_pattern
            idx += len(repeat_pattern)
        else:
            strinq += content[idx]
            idx += 1
    return len(strinq)

if __name__ == "__main__":
    print(solution('input.txt'))