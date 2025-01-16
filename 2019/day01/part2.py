import math

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    total_fuel = 0
    for mass in content:
        fuel = math.floor(int(mass) / 3) - 2
        total_fuel += fuel
        while fuel > 0:
            req_fuel = math.floor(fuel / 3) - 2
            if req_fuel > 0:
                total_fuel += req_fuel
            fuel = req_fuel
    return total_fuel

if __name__ == "__main__":
    print(solution('input.txt')) 