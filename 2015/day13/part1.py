from itertools import permutations

def x(fname):
    with open(fname) as f:
        content = f.read().splitlines()
    guests = set()
    happiness_dict = dict()
    for line in content:
        p1, state, points, p2 = line.split(' ')[0], line.split(' ')[2], line.split(' ')[3], line.split(' ')[-1][:-1]
        guests.add(p1)
        #print(p1, state, points, p2)
        if state == "lose":
            points = int(points) * -1
        else:
            points = int(points)
        try:
            happiness_dict[p1][p2] = points
        except:
            happiness_dict[p1] = {}
            happiness_dict[p1][p2] = points
    possible_arrangements = list(permutations(guests))
    max_happiness = float('-inf')
    for arrangement in possible_arrangements:
        happiness = 0
        for idx, person in enumerate(arrangement):
            happiness += happiness_dict[person][arrangement[idx - 1]]
            happiness += happiness_dict[person][arrangement[(idx + 1)%len(arrangement)]]

        if happiness > max_happiness:
            max_happiness = happiness
    return max_happiness

if __name__ == "__main__":
    print(x("input.txt"))