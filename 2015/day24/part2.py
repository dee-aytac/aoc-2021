import math
import itertools

def solution(fname):
    with open(fname) as f:
        content = f.read().splitlines()
    numbers = list()
    for line in content:
        numbers.append(int(line))
        
    minimum_package_no = 1
    minimums = list()
    not_found = True
    while not_found:
        combs = list(itertools.combinations((numbers), minimum_package_no))
        for c in combs:
            if sum(c) == sum(numbers) // 4:
                not_found = False
                minimums.append(c)
        minimum_package_no += 1
    min_eq = float("inf")
    for arrangment in minimums:
        if math.prod(arrangment) < min_eq:
            min_eq = math.prod(arrangment)
            m = arrangment
    return min_eq

if __name__ == "__main__":
    print(solution("input.txt"))

