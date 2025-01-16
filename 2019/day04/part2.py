
def solution(low, high):
    total_valid_pw = 0
    for num in range(low, high + 1):
        adjacent = False
        decreasing = False
        repeating_chars = set()
        for idx in range(len(str(num)) - 1):
            if str(num)[idx] == str(num)[idx + 1]:
                adjacent = True
                repeating_chars.add(str(num)[idx])
            if int(str(num)[idx]) > int(str(num)[idx + 1]):
                decreasing = True
        valid = False
        if adjacent:
            for char in repeating_chars:
                if str(num).count(char) == 2:
                    valid = True
                    break
                if str(num).count(char) > 2:
                    valid = False
        if adjacent == True and decreasing == False and valid:
            total_valid_pw += 1
    return total_valid_pw


if __name__ == "__main__":
    print(solution(153517, 630395)) 

