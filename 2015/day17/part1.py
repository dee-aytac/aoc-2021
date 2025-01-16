
def recursive(arr, total, idx):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif idx < 0:
        return 0
    if total < arr[idx]:
        return recursive(arr, total, idx - 1)
    else:
        return recursive(arr, total-arr[idx], idx - 1) +recursive(arr, total, idx - 1)

def solution(fname, goal):
    eggnog = list()
    with open(fname) as f:
        content = f.read().splitlines()
    for line in content:
        eggnog.append(int(line))
    eggnog.sort()
    return recursive(eggnog, goal, len(eggnog) - 1)


if __name__ == "__main__":
    print(solution("input.txt", 150))

