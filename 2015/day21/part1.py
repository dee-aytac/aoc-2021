from copy import deepcopy

def battle(player, enemy):
    l_player = deepcopy(player)
    l_enemy = deepcopy(enemy)
    while True:
        l_enemy["Hit Points"] -= max(l_player["Damage"] - l_enemy["Armor"], 1)
        if l_enemy["Hit Points"] <= 0:
            return "player"
        l_player["Hit Points"] -= max(l_enemy["Damage"] - l_player["Armor"], 1)
        if l_player["Hit Points"] <= 0:
            return "enemy"

def solution(fname):
    weapons = {"Dagger": {"cost": 8, "damage": 4, "armor": 0},
    "Shortsword": {"cost": 10, "damage": 5, "armor": 0},
    "Warhammer": {"cost": 25, "damage": 6, "armor": 0},
    "Longsword": {"cost": 40, "damage": 7, "armor": 0},
    "Greataxe": {"cost": 74, "damage": 8, "armor": 0},
    }
    armors = {"Leather": {"cost": 13, "damage": 0, "armor": 1},
    "Chainmail": {"cost": 31, "damage": 0, "armor": 2},
    "Splintmail": {"cost": 53, "damage": 0, "armor": 3},
    "Bandedmail": {"cost": 75, "damage": 0, "armor": 4},
    "Platemail": {"cost": 102, "damage": 0, "armor": 5},
    "None": {"cost": 0, "damage": 0, "armor": 0},
    }
    rings = {"Damage +1": {"cost": 25, "damage": 1, "armor": 0},
    "Damage +2": {"cost": 50, "damage": 2, "armor": 0},
    "Damage +3": {"cost": 100, "damage": 3, "armor": 0},
    "Defense +1": {"cost": 20, "damage": 0, "armor": 1},
    "Defense +2": {"cost": 40, "damage": 0, "armor": 2},
    "Defense +3": {"cost": 80, "damage": 0, "armor": 3},
    "None": {"cost": 0, "damage": 0, "armor": 0},
    }
    with open(fname) as f:
        content = f.read().splitlines()
    enemy = dict()
    for idx in range(len(content)):
        key, val = content[idx].split(':')
        enemy[key] = int(val)
    min_cost = float('inf')
    for key1, weapon in weapons.items():
        for key2, armor in armors.items():
            for key3, ring1 in rings.items():
                for key4, ring2 in rings.items():
                    if (key3 == key4) and key3 != "None":
                        continue
                    else:
                        total_cost = 0
                        player = {'Hit Points': 100, 'Damage': 0, 'Armor': 0}
                        player['Armor'] += armor["armor"] + ring1["armor"] + ring2["armor"]
                        player['Damage'] += weapon["damage"] + ring1["damage"] + ring2["damage"]
                        total_cost = weapons[key1]["cost"] + armors[key2]["cost"] + rings[key3]["cost"] + rings[key4]["cost"]
                        winner = battle(player, enemy)
                        if winner == "player":
                            if total_cost < min_cost:
                                min_cost = total_cost
    return min_cost

if __name__ == "__main__":
    print(solution("input.txt"))

