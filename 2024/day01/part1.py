
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    calibration_sum = 0
    left_list = list()
    right_list = list()
    for line in content:
        n1, n2 = line.split('   ')
        left_list.append(int(n1))
        right_list.append(int(n2))
    left_list = sorted(left_list)
    right_list = sorted(right_list)
    total_distance = 0
    for idx in range(0,len(left_list)):
        total_distance += abs(left_list[idx] - right_list[idx])
        print(left_list[idx], right_list[idx])
    return total_distance

if __name__ == "__main__":
    print(solution('input.txt')) 
