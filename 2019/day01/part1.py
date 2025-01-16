import math

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    total_fuel = 0
    for mass in content:
        total_fuel += math.floor(int(mass) / 3) - 2
    return total_fuel
if __name__ == "__main__":
    print(solution('input.txt')) 