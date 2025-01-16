
def get_parents(dictionary, key):
    curr_key = dictionary[key]
    parents = list()
    while True:
        if curr_key not in dictionary.keys():
            break
        else:
            parents.append(curr_key)
        curr_key = dictionary[curr_key]
    return parents


def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    nodes = dict()
    for line in content:
        root, node = line.split(')')
        nodes[node] = root
    you_parens = get_parents(nodes, "YOU")
    san_parens = get_parents(nodes, "SAN")
    common_paths = set(you_parens).intersection(set(san_parens))
    return min([you_parens.index(path) + san_parens.index(path) for path in common_paths]) 

if __name__ == "__main__":
    print(solution('input.txt')) 
