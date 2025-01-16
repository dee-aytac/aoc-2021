
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    calibration_sum = 0
    for line in content:
        last_char = None
        for char in line:
            if char.isdigit():
                if last_char == None:
                    calibration_sum += int(char) * 10
                last_char = char 
        calibration_sum += int(last_char)
        print(calibration_sum)
    return calibration_sum
if __name__ == "__main__":
    print(solution('input.txt')) 
