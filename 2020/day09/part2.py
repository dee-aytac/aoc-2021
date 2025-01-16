
def get_sum(arr, wanted_num):
    idx = 0
    for idx in range(len(arr) - 1):
        length = 2
        while True:
            if idx + length > len(arr):
                break
            if sum(arr[idx:idx+length]) == wanted_num:
                return arr[idx:idx+length]
            length += 1

def check_two_sum(arr, wanted_num):
    nums = set()
    for num in arr:
        if (wanted_num - num) in nums:
            return True
        nums.add(num)
    return False

def solution(fname, preamble):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    arr = list()
    idx = 0
    invalid_num = -1
    while idx < len(content):
        num = int(content[idx])
        if idx >= preamble:
            if check_two_sum(arr, num):
                pass
            else:
                invalid_num = num
                break
        arr.append(num)
        if len(arr) == preamble + 1:
            arr = arr[1:]
        idx += 1
    array_totalling = sorted(get_sum([int(num) for num in content], invalid_num))
    return array_totalling[0] + array_totalling[-1]

if __name__ == "__main__":
    print(solution('input.txt', 25)) 
