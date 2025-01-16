
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    sum_of_ids = 0
    for line in content:
        valid_game = True
        inventory = {"blue": 14, "red": 12, "green": 13}
        current_id = line.split(":")[0][len("Game "):]
        current_sets = line.split(": ")[1].split("; ")
        for current_set in current_sets:
            for item in current_set.split(", "):
                for key in inventory.keys():
                    if key in item:
                        count = item[:item.index(key)]
                        if inventory[key] - int(count) < 0:
                            valid_game = False
        if valid_game:
            sum_of_ids += int(current_id)
    return sum_of_ids
    
if __name__ == "__main__":
    print(solution('input.txt')) 
