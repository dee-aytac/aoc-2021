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

def calculate(numbers_):
    numbers = deepcopy(numbers_)
    total_distribution = 0
    seen = list()
    while True:
        index_max = get_index_of_max(numbers)
        numbers = distribute(numbers, index_max)
        total_distribution += 1
        if numbers in seen:
            return (numbers, total_distribution - 1)
        seen.append(numbers)

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    content = [line.split('\t') for line in content][0]
    content = [int(num) for num in content]
    first_state = calculate(content)
    return calculate(first_state[0])[1]

if __name__ == "__main__":
    print(solution('input.txt'))