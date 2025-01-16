import hashlib

def solution(puzzle_inp):
    answer = ""
    idx = 0
    while len(answer) < 8:
        new_inp = (puzzle_inp + str(idx)).encode()
        new_hash = hashlib.md5(new_inp).hexdigest()
        if new_hash[:5] == "00000":
            answer += str(new_hash[5])
            print(f"Found interesting hash {new_hash} with index: {idx}. New password layout is {answer}")
        idx += 1
    return answer

if __name__ == "__main__":
    puzzle_input = "ffykfhsq"
    print(f"The password is: {solution(puzzle_input)}")
