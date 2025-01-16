
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    common = ""
    total_length = len(content)
    str_length = len(content[0])
    for self_idx in range(0, total_length):
        for other_idx in range(self_idx + 1, total_length):
            difference = 0
            for char_idx in range(str_length):
                if difference > 1:
                    break
                if content[self_idx][char_idx] == content[other_idx][char_idx]:
                    continue
                else:
                    dif_idx = char_idx
                    difference += 1
            if difference <= 1:
                return content[self_idx][:dif_idx] + content[self_idx][dif_idx+1:]

if __name__ == "__main__":
    print(solution('input.txt'))