from itertools import permutations

def longest_path(fname):
    roads = set()
    towns = set()
    for line in open(fname):
        p1, p2 = line.strip('\n').split(" = ")
        city1, city2 = p1.split(" to ")
        distance = int(p2)
        towns.add(city1)
        towns.add(city2)
        roads.add((city1, city2, distance))

    longest_path = float('-inf')
    for possible_road in list(permutations(towns)):
        local_cost = 0
        for i in range(len(possible_road) - 1):
            not_found = True
            while not_found:
                for way in roads:
                    if way[0] == possible_road[i] and way[1] == possible_road[i+1]:
                        local_cost += way[2]
                        not_found = False
                        continue
                    if way[1] == possible_road[i] and way[0] == possible_road[i+1]:
                        not_found = False
                        local_cost += way[2]
                        continue
                        
        if local_cost > longest_path:
            longest_path = local_cost  
    return longest_path

if __name__ == "__main__":
    print(longest_path('input.txt'))