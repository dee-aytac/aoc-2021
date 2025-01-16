from collections import defaultdict

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    nums = [int(num) for num in content]
    nums.sort()
    nums.append(nums[-1] + 3)
    nums.append(0)
    nums.sort()

    possible_paths = defaultdict(int)
    possible_paths[0] = 1
    for num in nums:
        for offset in range(1, 4):
            possible_num = num + offset
            if possible_num in nums:
                possible_paths[possible_num] += possible_paths[num] 
    return possible_paths[nums[-1]]

if __name__ == "__main__":
    print(solution('input.txt')) 
