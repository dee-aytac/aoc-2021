
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    nums = [int(num) for num in content]
    nums.sort()
    biggest = nums[-1] + 3
    nums.append(biggest)
    current_jolt = 0
    idx = 0
    one_diff = 0
    three_dif = 0
    while idx < len(nums):
        num = nums[idx]
        if num - current_jolt == 1:
            one_diff += 1
        elif num - current_jolt == 3:
            three_dif += 1
        else:
            print("error", num - current_jolt)
        current_jolt = num
        idx +=1 
    return one_diff * three_dif
if __name__ == "__main__":
    print(solution('input.txt')) 
