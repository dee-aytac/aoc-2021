
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    nodes = dict()
    for line in content:
        root, node = line.split(')')
        nodes[node] = root
    total_orbits = 0
    for key in nodes.keys():
        curr_key = key
        while True:
            if curr_key not in nodes.keys():
                break
            else:
                total_orbits += 1
            curr_key = nodes[curr_key]
    return total_orbits

if __name__ == "__main__":
    print(solution('input.txt')) 
