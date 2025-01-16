
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    sum_of_power = 0
    for line in content:
        inventory = {"blue": 0, "red": 0, "green": 0}
        current_id = line.split(":")[0][len("Game "):]
        current_sets = line.split(": ")[1].split("; ")
        for current_set in current_sets:
            for item in current_set.split(", "):
                for key in inventory.keys():
                    if key in item:
                        count = item[:item.index(key)]
                        inventory[key] = max(inventory[key],int(count))
        sum_of_power += inventory["blue"] * inventory["red"] * inventory["green"]
    return sum_of_power
    
if __name__ == "__main__":
    print(solution('input.txt')) 
