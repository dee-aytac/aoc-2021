
def solution(fname):
    best_score = float('-inf')
    with open(fname) as f:
        content = f.read().splitlines()
    ingredients = dict()
    for line in content:
        ingredients[line.split(' ')[0][:-1]] = {
            line.split(' ')[1]: int(line.split(' ')[2][:-1]), 
            line.split(' ')[3]: int(line.split(' ')[4][:-1]),
            line.split(' ')[5]: int(line.split(' ')[6][:-1]),
            line.split(' ')[7]: int(line.split(' ')[8][:-1]),
            line.split(' ')[9]: int(line.split(' ')[10]),
            }

    for i in range(0, 100):
        for j in range(0, (100 - i) + 1):
            for k in range(0, 100 - (i - j) + 1):
                l = 100 - i - j - k
                p1 = ingredients["Sprinkles"]["capacity"] * i + ingredients["PeanutButter"]["capacity"] * j + ingredients["Frosting"]["capacity"] * k + ingredients["Sugar"]["capacity"] * l
                p2  = ingredients["Sprinkles"]["durability"] * i + ingredients["PeanutButter"]["durability"] * j + ingredients["Frosting"]["durability"] * k + ingredients["Sugar"]["durability"] * l
                p3 = ingredients["Sprinkles"]["flavor"] * i + ingredients["PeanutButter"]["flavor"] * j + ingredients["Frosting"]["flavor"] * k + ingredients["Sugar"]["flavor"] * l
                p4 = ingredients["Sprinkles"]["texture"] * i + ingredients["PeanutButter"]["texture"] * j + ingredients["Frosting"]["texture"] * k + ingredients["Sugar"]["texture"] * l
                calories = ingredients["Sprinkles"]["calories"] * i + ingredients["PeanutButter"]["calories"] * j + ingredients["Frosting"]["calories"] * k + ingredients["Sugar"]["calories"] * l
                if calories == 500:
                    if (p1 > 0) and (p2 > 0) and (p3 > 0) and (p4 > 0):
                        if (p1 * p2 * p3 * p4) > best_score:
                            best_score = (p1 * p2 * p3 * p4)
    return best_score

if __name__ == "__main__":
    print(solution("input.txt"))

