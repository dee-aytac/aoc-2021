
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    calibration_sum = 0
    text_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in content:
        digits = []
        for idx, char in enumerate(line):
            if char.isdigit():
                digits.append(int(char))
            else:
                for idx_num, number in enumerate(text_numbers):
                    if line[idx:idx+len(number)] == number:
                        digits.append(idx_num + 1)
        calibration_sum += digits[0] * 10 + digits[-1]

    return calibration_sum
if __name__ == "__main__":
    print(solution('input.txt')) 
