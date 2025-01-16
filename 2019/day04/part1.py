
def solution(low, high):
    total_valid_pw = 0
    for num in range(low, high + 1):
        adjacent = False
        decreasing = False
        for idx in range(len(str(num)) - 1):
            if str(num)[idx] == str(num)[idx + 1]:
                adjacent = True
            if int(str(num)[idx]) > int(str(num)[idx + 1]):
                decreasing = True
        if adjacent == True and decreasing == False:
            total_valid_pw += 1
    return total_valid_pw


if __name__ == "__main__":
    print(solution(153517, 630395)) 

