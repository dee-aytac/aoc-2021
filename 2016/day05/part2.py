import hashlib

def solution(puzzle_inp):
    answer = ['.', '.', '.', '.', '.', '.', '.', '.']
    idx = 0
    while '.' in answer:
        new_inp = (puzzle_inp + str(idx)).encode()
        new_hash = hashlib.md5(new_inp).hexdigest()
        if new_hash[:5] == "00000":
            try:
                new_pos, new_char = int(new_hash[5]), new_hash[6]
                if answer[new_pos] == '.':
                    answer[new_pos] = new_char
                    print(f"Found interesting hash {new_hash} with index: {idx}. New password layout is {''.join(answer)}")
            except:
                pass
        idx += 1
    return "".join(answer)

if __name__ == "__main__":
    puzzle_input = "ffykfhsq"
    print(f"The password is: {solution(puzzle_input)}")
 