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
    while idx < len(content):
        num = int(content[idx])
        if idx >= preamble:
            if check_two_sum(arr, num):
                pass
            else:
                return num
        arr.append(num)
        if len(arr) == preamble + 1:
            arr = arr[1:]
        idx += 1
if __name__ == "__main__":
    print(solution('input.txt', 25)) 
