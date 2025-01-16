from copy import deepcopy

def get_index_of_max(numbers):
    max_num = float("-inf")
    max_idx = -1
    for idx, num in enumerate(numbers):
        if num > max_num:
            max_num = num
            max_idx = idx
    return max_idx

def distribute(numbers_, max_idx):
    numbers = deepcopy(numbers_)
    curr_idx = max_idx
    curr_idx = curr_idx % len(numbers)
    for _ in range(numbers[max_idx] + 1):
        numbers[max_idx] -= 1
        numbers[curr_idx] += 1
        curr_idx = (curr_idx + 1) % len(numbers)
 
    return numbers
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    content = [line.split('\t') for line in content][0]
    content = [int(num) for num in content]
    total_distribution = 0
    seen = list()
    while True:
        index_max = get_index_of_max(content)
        content = distribute(content, index_max)
        total_distribution += 1
        if content in seen:
            return total_distribution
        seen.append(content)

if __name__ == "__main__":
    print(solution('input.txt'))