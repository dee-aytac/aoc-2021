
def to_int(s):
    if not ',' in s:
        return int(s)
    else:
        return int(s[:-1])

def solution(fname):
    with open(fname) as f:
        content = f.read().splitlines()
    real_aunt = {"children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    for line in content:
        aunt_no, items = line.split(": ")[0], line.split(": ")[1:]
        i = 0
        items = (" ".join(items))
        items = items.split(' ')
        correct = True
        while i < len(items):
            if items[i] == "trees" or items[i] == "cats":
                if real_aunt[items[i]] >= to_int(items[i + 1]):
                    correct = False
            elif items[i] == "pomeranians" or items[i] == "goldfish":
                if real_aunt[items[i]] <= to_int(items[i + 1]):
                    correct = False
            else:
                if real_aunt[items[i]] != to_int(items[i + 1]):
                    correct = False
            i += 2
        if correct == True:
            return aunt_no

if __name__ == "__main__":
    print(solution("input.txt"))

