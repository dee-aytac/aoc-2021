
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    calibration_sum = 0
    left_list = list()
    right_list = list()
    similarity_score = 0
    for line in content:
        n1, n2 = line.split('   ')
        left_list.append(int(n1))
        right_list.append(int(n2))
    left_list = sorted(left_list)
    right_list = sorted(right_list)
    total_distance = 0
    for idx, num in enumerate(left_list):
        similarity_score += right_list.count(num) * num
        print(num, right_list.count(num))
    return similarity_score

if __name__ == "__main__":
    print(solution('input.txt')) 
